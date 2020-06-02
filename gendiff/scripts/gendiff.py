# -*- coding: utf-8 -*-

"""The option parser."""

from gendiff.parser import parse_args
from gendiff.engine import build_diff


def main():
    options = parse_args()
    diff_string = build_diff(options.first_file,
                                options.second_file)


if __name__ == '__main__':
    main()
    
