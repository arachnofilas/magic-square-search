#!/usr/bin/python3

import argparse
import sys
import os
import numpy as np


def parser():
    parser = argparse.ArgumentParser(
        description='This tool searches for a number of magic squares ' +
        'in a given [n,m] matrix.')
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


def validate(rows, columns):
    if rows < 2 or columns < 2:
        print('Magic number cannot appear in a matrix which is ' +
        'smaller than [2,2]')
        sys.exit(1)


def generate_matrix(rows, columns):
    return np.random.randint(10, size=(rows, columns))


def main():
    args = parser()
    validate(args.rows, args.columns)
    matrix = generate_matrix(args.rows, args.columns)
    print(matrix)


if __name__ == '__main__':
    main()
