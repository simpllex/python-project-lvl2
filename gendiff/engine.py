import json
import os
import yaml


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


def build_diff(old, new):
    common = {}
    old_keys = set(old.keys())
    new_keys = set(new.keys())
    intersect_keys = sorted(old_keys & new_keys)
    common.update(
        {
            key: ('UNCHANGED', old[key])
            for key in intersect_keys if old[key] == new[key]
        },
    )
    common.update(
        {
            key: ('CHANGED', old[key], new[key])
            for key in intersect_keys if old[key] != new[key]
        },
    )
    removed = {key: old[key] for key in sorted(old_keys - new_keys)}
    common.update(
        {
            key: ('REMOVED', removed[key]) for key in removed
        },
    )
    added = {key: new[key] for key in sorted(new_keys - old_keys)}
    common.update(
        {
            key: ('ADDED', added[key]) for key in added
        },
    )
    for key in sorted(old.keys() & new.keys()):
        old_value = old.get(key)
        new_value = new.get(key)
        has_children = (
            isinstance(old_value, dict)
        ) and (
            isinstance(new_value, dict)
        )
        if has_children:
            common[key] = (
                "NESTED",
                build_diff(old_value, new_value),
            )
        elif old_value == new_value:
            common[key] = ("UNCHANGED", old_value)
        else:
            common[key] = ("CHANGED", old_value, new_value)
    return common


def convert_to_string(my_dict):
    my_str = []
    res = ''
    for key, value in my_dict.items():
        flag, rest = value[0], value[1:]
        if flag == "UNCHANGED":
            meaning = rest[0]
            mstr = join_str(" ", key, meaning)
            my_str.append(mstr)
        if flag == "ADDED":
            meaning = rest[0]
            mstr = join_str("+", key, meaning)
            my_str.append(mstr)
        if flag == "REMOVED":
            meaning = rest[0]
            mstr = join_str("-", key, meaning)
            my_str.append(mstr)
        if flag == "CHANGED":
            old_changed, new_changed = rest[0], rest[1]
            mstr = join_str("+", key, old_changed)
            my_str.append(mstr)
            mstr = join_str("-", key, new_changed)
            my_str.append(mstr)
        if flag == "NESTED":
            mstr = join_str(" ", key, convert_to_string(rest[0]))
            my_str.append(mstr)
        res = "{\n" + "\n".join(x for x in my_str) + "\n}"

    return res


def join_str(flag, key, value):
    if isinstance(value, dict):
        result = ""
        internal_values = []
        for inkey, inval in value.items():
            temp = "\t" + inkey + ": " + inval
            internal_values.append(temp)
        result = "{\n" + "\n".join(x for x in internal_values) + "\n  }"
        return (flag + " " + key + ": " + result)
    else:
        return (flag + " " + key + ": " + str(value))


def return_string(old, new):
    return convert_to_string(build_diff(old, new))
