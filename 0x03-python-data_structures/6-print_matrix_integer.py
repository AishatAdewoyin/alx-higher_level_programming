#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for c in range(len(matrix)):
        for x in range(len(matrix[c])):
            if x != 0:
                print(' {:d}'.format(matrix[c][x]), end='')
            else:
                print('{:d}'.format(matrix[c][x]), end='')
        print()
