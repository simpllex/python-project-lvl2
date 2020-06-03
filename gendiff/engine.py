# -*- coding: utf-8 -*-

"""The option parser."""

import json


def build_diff(old, new):
    """Build string difference from  two file.
    Args:
        path_to_file: path to file
    Returns:
           string
    """
    result =""
    old = read_file(old)
    new = read_file(new)
    old_keys = set(old.keys())
    new_keys = set(new.keys())
    intersect_keys = old_keys & new_keys
    removed = old_keys - new_keys
    removed = {o : old[o] for o in removed}
    result += convert_to_string(removed)
    added = new_keys - old_keys
    added = {o : new[o] for o in added}
    result += convert_to_string(added)
    modified_old = {o : old[o] for o in intersect_keys if old[o] != new[o]}
    result += convert_to_string(modified_old)
    modified_new = {o : new[o] for o in intersect_keys if old[o] != new[o]}
    result += convert_to_string(modified_new)
    same = {o : old[o] for o in intersect_keys if old[o] == new[o]}
    result += convert_to_string(same)
    print("{\n" + result + "\n}")
    return ("{\n" + result + "\n}")
    

def read_file(file):
    """Get dictionary from file.
    Args:
        path_to_file: path to file
    Returns:
        formatted data
    """
    return json.load(open(file))


def convert_to_string(my_dict):
    """Get string from dictionary.
    Args:
        dictionary
    Returns:
        string
    """
    my_str = ''
    for key, value in my_dict.items():
        my_str = key + ' : ' + str(value) + " "
    return my_str
 