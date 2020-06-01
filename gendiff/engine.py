import json


def puf(old, new):
    old = read_file(old)
    new = read_file(new)
    a = set(old)
    b = set(new)
    d = dict()
    d[""] = a & b
    d["+"] = b - a
    d["-"] = a - b
    print(d)

def read_file(file):
    return json.load(open(file))
