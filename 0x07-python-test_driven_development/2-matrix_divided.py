#!/usr/bin/python3
"""

This module is a function that divides the numbers of a matrix

"""


def matrix_divided(matrix, div):
    """ function that divides the integer/float numbers of a matrix

    Args:
        matrix: list of a lists of integers/floats
        div: number which divides the matrix

    Returns:
        new matrix with the result of the division

    Raises:
        TypeError: If the elements of the matrix aren't lists
                   If the elemetns of the lists aren't integers/floats
                   If div is not an integer/float number
                   If the lists of the matrix don't have the same size

        ZeroDivisionError: If div is zero


    """

    if not type(div) in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    messg_type = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(messg_type)

    elem_len = 0
    messg_size = "Each row of the matrix must have the same size"

    for elem in matrix:
        if not elem or not isinstance(elem, list):
            raise TypeError(messg_type)

        if elem_len != 0 and len(elem) != elem_len:
            raise TypeError(messg_size)

        for number in elem:
            if not type(number) in (int, float):
                raise TypeError(messg_type)

        elem_len = len(elem)

    m = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return (m)
