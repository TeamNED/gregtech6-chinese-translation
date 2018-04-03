#-*- coding：utf-8 -*-

import logging
import sys
from source.utilities import mclang
from source.replacer.glossary import get_item_by_key


class Translator:
    """A translator using pre-defined glossary and patterns"""

    def __init__(self, glossary, patterns):
        """Initiates a new translator

        Args:
            glossary (dict): pre-defined glossary.
            patterns (list of pattern): pre-defined patterns."""

        self.glossary = glossary
        self.patterns = patterns

    def translate(self, key, value, logging_predicate=None):
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
        return self._find_possible_translation(key, value, None, filtered_patterns, logging_predicate)

    def _find_possible_translation(self, key, value, token, patterns, logging_predicate=None):
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
        logger = None
        if logging_predicate and logging_predicate(key):
            logger = logging.getLogger('translator')
            logger.debug(
                "key={0},value={1},token={2}".format(key, value, token), extra={'event': 'TRANSLATING'})
            if patterns:
                for pattern in patterns:
                    logger.debug("({0}->{1}) as <{2}> @{3} #{4}".format(
                        pattern.value, pattern.repl, pattern.token, pattern.key, pattern.priority), extra={'event': 'PATTERN_LOAD'})
            else:
                logger.debug("", extra={'event': 'NO_PATTERN'})

        # find glossary
        if(token in self.glossary and value in self.glossary[token]):
            if type(self.glossary[token]) is dict:
                result = get_item_by_key(self.glossary[token], value, key)
            else:
                result = self.glossary[token][value]

            if logger:
                if result:
                    logger.debug("Found as <{0}>".format(
                        self.glossary[token][value]), extra={'event': 'GLOSSARY'})
                else:
                    logger.warning("Not found", extra={'event': 'GLOSSARY'})
            return result

        if not patterns:
            return None

        for index in range(0, len(patterns)):
            current_pattern = patterns[index]
            status, match_result = current_pattern.match_value(value)
            if(status):

                if logger:
                    logger.debug("({0}->{1}) as <{2}> @{3} #{4}".format
                                 (current_pattern.value, current_pattern.repl, current_pattern.token,
                                  current_pattern.key, current_pattern.priority), extra={'event': 'PATTERN_USING'})

                succ = 1  # Flag for all token-value has translated
                token_dict = {}
                if(match_result):
                    for t, v in match_result.items():
                        # Find All tokens' tranlation
                        find_result = self._find_possible_translation(
                            key, v, t, patterns[index+1:], logging_predicate)
                        if find_result:
                            token_dict[t] = find_result
                        else:
                            succ = 0  # Match failed

                            if logger:
                                logger.debug("({0}->{1}) as <{2}> @{3} #{4}".format
                                             (current_pattern.value, current_pattern.repl, current_pattern.token,
                                              current_pattern.key, current_pattern.priority), extra={'event': 'PATTERN_FAIL'})
                            break
                    if(succ):
                        # Add the result to glossary as a cache
                        result = current_pattern.format(token_dict)

                        if logger:
                            logger.debug(
                                "Item translated as <{0}>".format(result), extra={'event': "SUCCESS"})

                        self.glossary.setdefault(current_pattern.token, {})[
                            value] = result
                        return result
                else:
                    if(current_pattern.repl.find('{') == -1 and current_pattern.repl.find('}') == -1):
                        # No token needed
                        result = current_pattern.repl
                        self.glossary.setdefault(current_pattern.token, {})[
                            value] = result

                        if logger:
                            logger.debug(
                                "Item translated as <{0}>".format(result), extra={'event': "SUCCESS"})

                        return result
                    else:

                        if logger:
                            logger.warning(
                                "No enough token translated", extra={'event': "FAILED"})

                        return None

        if logger:
            logger.warning("Patterns ALL FAILED", extra={'event': "FAILED"})

        return None  # All patterns failed
