# -*- coding：utf-8 -*-

import re


def dict_split(dic, config):
    """Split a dict into many patitons, first-served basis

    Args:
        dic (dict): (k,v) pairs
        config (list): list of {name,regex} dict telling how to split

    Returns:
        {name:{k,v that matches regex}}"""

    result = {}
    for k, v in dic.items():
        group_name = _dict_split_judge_key(k, config)
        result.setdefault(group_name, {})[k] = v
    return result


def _dict_split_judge_key(key, config):
    """Judge the group name of a key

    Args:
        key (str): the key you want to judge
        config (list): list of {name,regex} dict telling how to split

    Returns:
        the group name you want"""
    return next((x['name'] for x in config if re.match(x['regex'], key)), None)
