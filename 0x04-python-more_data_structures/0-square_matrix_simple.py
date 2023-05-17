#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    nw_matrix = matrix.copy()

    for m in range(len(matrix)):
        nw_matrix[m] = list(map(lambda x: x**2, matrix[m]))

    return (nw_matrix)
