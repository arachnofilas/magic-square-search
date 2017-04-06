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
        print('Magic square cannot appear in a matrix which is ' +
        'smaller than [2,2]')
        sys.exit(1)
        '''
        fixed type "magic number" to "magic square"
        '''

def generate_matrix(rows, columns):
    return np.random.randint(10, size=(rows, columns))


def get_square_matrix_from(matrix):
    rows = matrix.shape[0]
    columns = matrix.shape[1]
    #print('Rows: ' + str(rows) + '; Columns: ' + str(columns))
    max_square_dimension = get_max_square_dimension(matrix)
    #print('Max square dimension is: ' + str(max_square_dimension))
    i = 1
    for square_dimension in range(2,max_square_dimension+1):
        for row in range(rows):
            for column in range(columns):
                if row < rows - i and column < columns - i:
                    temp = matrix[row:row+square_dimension,column:column+square_dimension]
                    print(temp)
                else:
                    break
        i += 1


def get_max_square_dimension(matrix):
    rows = matrix.shape[0]
    columns = matrix.shape[1]
    max_dimension = rows
    if columns < rows:
        max_dimension = columns
    return max_dimension


def main():
    args = parser()
    validate(args.rows, args.columns)
    matrix = generate_matrix(args.rows, args.columns)
    print(matrix)
    get_square_matrix_from(matrix)
    '''
    jei sukurta matrica iskart square tai pirma mest i is_magic_square, tik po to i get_square_matrix_from
    '''


if __name__ == '__main__':
    main()
