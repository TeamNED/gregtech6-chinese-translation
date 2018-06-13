# -*- coding：utf-8 -*-


def mclang_to_dict(text, filter=None):
    """Convert Minecraft Language File to dict

    Args:
        text (list): the content of mclang
        filter (lambda str:bool) : returns ture if you want to make an item in your dict, set to None if you want everything in

    Returns:
        the dict of your mclang"""

    result = {}
    for line in text:
        if (filter is None or filter(line)) and line.find('=') != -1:
            k, v = line.split('=', maxsplit=1)
            result[k.strip()] = v.strip()

    return result
