import json
import os
import yaml


def build_diff(old, new):
    result = ""
    old = read_file(old)
    new = read_file(new)
    old_keys = set(old.keys())
    new_keys = set(new.keys())
    intersect_keys = old_keys & new_keys
    removed = old_keys - new_keys
    removed = {key: old[key] for key in removed}
    result += convert_to_string(removed)
    added = new_keys - old_keys
    added = {key: new[key] for key in added}
    result += convert_to_string(added)
    modified_old = {o: old[o] for o in intersect_keys if old[o] != new[o]}
    result += convert_to_string(modified_old)
    modified_new = {o: new[o] for o in intersect_keys if old[o] != new[o]}
    result += convert_to_string(modified_new)
    same = {key: old[key] for key in intersect_keys if old[key] == new[key]}
    result += convert_to_string(same)
    return ("{\n" + result + "\n}")


def read_file(path):
    if not os.path.isabs(path):
        path = os.path.join(os.getcwd(), path)
    _, file_type = os.path.splitext(path)
    if file_type == '.json':
        return json.load(open(path))
    elif file_type == '.yml':
        return yaml.load(open(path), Loader=yaml.Loader)
    else:
        raise Exception("Invalid format, run --help!")


def convert_to_string(my_dict):
    my_str = ''
    for key, value in my_dict.items():
        my_str = key + ' : ' + str(value) + " "
    return my_str
