# -*- coding：utf-8 -*-

import re


class Pattern:
    """Regex pattern used by translator"""

    def __init__(self, key, value, token, repl, priority):
        """Inititates a new patttern

        Args:
            key (str): regex string matches the key of an item
            value (str): regex string matches the value of an item, using captrue groups with "name",... to get the corresponding tranlated head in repl
            token (str): main token of an item
            repl (str): string for the output of an item, using placeholders "{name}",... which will be replaced if captured
            priority (int): patterns with a higher priority will be executed first"""

        self.key = key
        self.key_rg = None
        self.value = value
        self.value_rg = None
        self.token = token
        self.repl = repl
        self.priority = priority

    def match_key(self, key):
        """Try to match the key of an item in language file

        Args:
            key (str): the key of the item

        Returns:
            true if matched, false otherwise"""
        # Try to match key
        if (self.key_rg is None):
            self.key_rg = re.compile(self.key)

        return self.key_rg.match(key) is not None

    def match_value(self, value):
        """Try to match the value of an item in language file

        Args:
            value (str): the value of the item

        Returns:
            (code, dict)
                code (bool): True if successfully matched
                dict: head-value dict which might be None"""

        # Try to match value
        if (self.value_rg is None):
            self.value_rg = re.compile(self.value)

        match_result = self.value_rg.match(value)
        if (match_result is not None):
            return (True, match_result.groupdict())
        else:
            return (False, None)

    def format(self, token_dict):
        """ Get formatted value with a given glossary

        Args:
            token_dict (dict): an dict of token-values"""

        return self.repl.format(**token_dict)
