#!/usr/bin/python3

import argparse
import sys
import os

def parser():
    parser = argparse.ArgumentParser(
        description='This tool searches for a number of magic squares ' +
        'in a given [n,m] matrix.')
    parser.add_argument(
        'file',
        metavar='file',
        type=str,
        help='File to search in'
        )
    parser.add_argument(
        'rows',
        metavar='rows',
        type=int,
        help='Rows of the matrix'
    )
    parser.add_argument(
        'columns',
        metavar='columns',
        type=int,
        help='Columns of the matrix'
    )
    return parser.parse_args()


def initiate_search():
    args = parser()


if __name__ == '__main__':
    initiate_search()
