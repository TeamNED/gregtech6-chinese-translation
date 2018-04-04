#-*- coding：utf-8 -*-

import logging
import sys

from source.replacer.glossary import get_item_by_key
from source.utilities import mclang


class Translator:
    """A translator using pre-defined glossary and patterns"""

    def __init__(self, glossary, patterns):
        """Initiates a new translator

        Args:
            glossary (dict): pre-defined glossary.
            patterns (list of pattern): pre-defined patterns."""

        self.glossary = glossary
        self.patterns = patterns

    def translate(self, key, value):
        """
        Try to translate with given glossary and patterns

        Args:
            key (str): the key of the item
            value (str): the value of the item

        Returns:
            None if either key unmatched or any head failed to translate
            Translated value of the item otherwise"""
        filtered_patterns = sorted(filter(lambda x: x.match_key(
            key), self.patterns), key=lambda x: x.priority, reverse=True)
        return self._find_possible_translation(key, value, 'TOP_LEVEL', filtered_patterns)

    def _find_possible_translation(self, key, value, token, patterns):
        """A greed algorithm to find a possibletranslation within and patterns and with higeset total priority

        Args:
            key (str): the key of the item
            value (str): the value of the item
            token (str): token of match heads, set to None for first-run
            patterns (list of pattern): patterns you want to use.

        Returns:
            None if either key unmatched or any head failed to translate
            str of tranlation otherwise"""

        # logging
        logger = logging.getLogger(__name__)
        logger_event_base = {'key': key, 'value': value, 'token': token}

        logger.debug("key=%s,value=%s,token=%s", key, value, token, extra={
                     'event': 'TRANSLATING', **logger_event_base})
        if patterns:
            for pattern in patterns:
                self._log_pattern_status(
                    logger, logger_event_base, pattern, 'PATTERN_LOAD')
        else:
            logger.debug(
                "", extra={'event': 'NO_PATTERN', **logger_event_base})

        # find glossary
        if(token in self.glossary and value in self.glossary[token]):
            if type(self.glossary[token]) is dict:
                # if contains regexes and values
                result = get_item_by_key(self.glossary[token], value, key)
            else:
                result = self.glossary[token][value]

            if result:
                logger.debug("Found as <{}>".format(
                    self.glossary[token][value]), extra={'event': 'GLOSSARY', **logger_event_base})
            else:
                logger.warning("Not found", extra={
                    'event': 'GLOSSARY', **logger_event_base})
            return result

        if not patterns:
            logger.debug(
                "Neither patterns nor glossary matched this item", extra={'event': 'FAILED', **logger_event_base})
            return None

        for index in range(0, len(patterns)):
            current_pattern = patterns[index]
            status, match_result = current_pattern.match_value(value)
            if(status):
                self._log_pattern_status(
                    logger, logger_event_base, current_pattern, 'PATTERN_USING')

                succ = 1  # Flag for all token-value has translated
                token_dict = {}
                if(match_result):
                    for t, v in match_result.items():
                        # Find All tokens' tranlation
                        find_result = self._find_possible_translation(
                            key, v, t, patterns[index+1:])
                        if find_result:
                            token_dict[t] = find_result
                        else:
                            succ = 0  # Match failed

                            self._log_pattern_status(
                                logger, logger_event_base, current_pattern, 'PATTERN_FAIL')
                    if(succ):
                        # Add the result to glossary as a cache
                        result = current_pattern.format(token_dict)

                        logger.debug("Item translated as <{0}>".format(
                            result), extra={'event': "SUCCESS", **logger_event_base})

                        self.glossary.setdefault(current_pattern.token, {})[
                            value] = result
                        return result
                else:
                    if(current_pattern.repl.find('{') == -1 and current_pattern.repl.find('}') == -1):
                        # No token needed
                        result = current_pattern.repl
                        self.glossary.setdefault(current_pattern.token, {})[
                            value] = result

                        logger.debug("Item translated as <{0}>".format(
                            result), extra={'event': "SUCCESS", **logger_event_base})

                        return result
                    else:

                        logger.warning("No enough token translated", extra={
                                       'event': "FAILED", **logger_event_base})

                        return None

        logger.warning("Patterns ALL FAILED", extra={
                       'event': "FAILED", **logger_event_base})

        return None  # All patterns failed

    def _log_pattern_status(self, logger, logger_event_base, pattern, event, level=logging.DEBUG):
        """Log on the logger of an event concerning pattern

        Args:
            logger (logging.Logger): the logger you want to log on
            logger_event_base (dict): a dict containing keys: 'key','value' and 'token'
            pattern (replacer.Pattern): the pattern that you concerning
            event (str): which tells what happens
            level (int): level of LogRecord sent to logger, default is DEBUG

        Returns:
            None
        """
        logger.log(level, "%s --> %s as <%s> @%s #%s", pattern.value, pattern.repl, pattern.token,
                   pattern.key, pattern.priority, extra={'event': event, **logger_event_base})
