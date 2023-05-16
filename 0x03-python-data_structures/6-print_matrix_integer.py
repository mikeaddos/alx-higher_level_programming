#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for m in range(len(matrix)):
        for k in range(len(matrix[m])):
            if k != 0:
                print(" ", end='')
            print("{:d}".format(matrix[m][k]), end='')
        print()
