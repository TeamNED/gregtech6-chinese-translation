#-*- coding：utf-8 -*-

import re


def get_item_by_key(self, name, key):
    """Get the item with the corresponding name and key

    Args:
        name (str): name you want to search
        key (str): key of your name,

    Returns:
        you value, None if not found

    Examples:
        Iron_zh_cn=glossary.get_item_by_key('Iron','gt.material') """
    if name in self.keys():
        if type(self[name]) is str:
            return self[name]
        else:
            return next((x['value'] for x in self[name] if re.match(x['regex'], key)), None)
    else:
        return None
