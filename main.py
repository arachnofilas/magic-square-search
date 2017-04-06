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


def generate_matrix(rows, columns):
    return np.random.randint(10, size=(rows, columns))


def get_square_matrix_from(matrix,magic_square_counter):
    rows = matrix.shape[0]
    columns = matrix.shape[1]
    max_square_dimension = get_max_square_dimension(matrix)
    i = 1
    for square_dimension in range(2,max_square_dimension+1):
        for row in range(rows):
            for column in range(columns):
                if row < rows - i and column < columns - i:
                    temp_matrix = matrix[row:row+square_dimension,
                        column:column+square_dimension]
                    if is_magic_square(temp_matrix):
                        magic_square_counter += 1
                        if magic_square_counter > 0:
                            print(str(temp_matrix) + '\n')
                        else:
                            print('There are no magic squares')
                else:
                    break
        i += 1
    print('Total number of magic squares: ' + str(magic_square_counter) + '\n')


def get_max_square_dimension(matrix):
    rows = matrix.shape[0]
    columns = matrix.shape[1]
    max_dimension = rows
    if columns < rows:
        max_dimension = columns
    return max_dimension


def is_magic_square(square_matrix):
    rows = square_matrix.shape[0]
    columns = square_matrix.shape[1]
    first_diagonal = square_matrix.diagonal()
    second_diagonal = np.fliplr(square_matrix).diagonal()
    magic_sum = []
    temp_sum = 0
    for row in range(rows):
        for column in range(columns):
            temp_sum += square_matrix[row,column]
        magic_sum.append(temp_sum)
        temp_sum = 0
    for column in range(columns):
        for row in range(rows):
            temp_sum += square_matrix[row,column]
        magic_sum.append(temp_sum)
        temp_sum = 0
    for argument in range(first_diagonal.shape[0]):
        temp_sum += first_diagonal[argument]
    magic_sum.append(temp_sum)
    temp_sum = 0
    for argument in range(second_diagonal.shape[0]):
        temp_sum += second_diagonal[argument]
    magic_sum.append(temp_sum)
    temp_sum = 0
    return all(magic_sum[0] == value for value in magic_sum)


def main():
    args = parser()
    validate(args.rows, args.columns)
    matrix = generate_matrix(args.rows, args.columns)
    print('\nGenerated matrix: \n\n'+ str(matrix) + '\n')
    print('Magic squares:\n')
    magic_square_counter = 0
    get_square_matrix_from(matrix,magic_square_counter)

    #my_matrix = np.array([[4, 9, 2, 3, 5], [3, 5, 7, 4, 2], [8, 1, 6, 6, 2], [1, 1, 6, 6, 2]])
    #print('\nMy matrix: \n\n'+ str(my_matrix) + '\n')
    #get_square_matrix_from(my_matrix,magic_square_counter)


if __name__ == '__main__':
    main()
