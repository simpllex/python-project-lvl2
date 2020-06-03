# -*- coding: utf-8 -*-

"""The option parser."""

import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str, help='')
    parser.add_argument('second_file', type=str, help='')
    parser.add_argument('-f', '--format', default='plain',
                        help='set format of output (default: plain)')
    return parser.parse_args()
