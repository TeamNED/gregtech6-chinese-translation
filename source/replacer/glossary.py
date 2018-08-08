# -*- coding：utf-8 -*-

import re


def get_item_by_key(glossary, name, key):
    """Get the item with the corresponding name and key

    Args:
        glossary (dict): a dict containing original words and their corresponding translated words 
        name (str): name you want to search
        key (str): key of your name

    Returns:
        you value, None if not found

    Examples:
        Iron_zh_cn=glossary.get_item_by_key('Iron','gt.material') """
    if name in glossary.keys():
        if type(glossary[name]) is str:
            return glossary[name]
        else:
            return next((x['value'] for x in glossary[name] if re.match(x['regex'], key)), None)
    else:
        return None
