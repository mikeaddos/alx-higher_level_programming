#!/usr/bin/python3
"""

This module is a function that prints a square with the character #

"""


def print_square(size):
    """ function that prints a square with the character #

    Args:
        size: size of the square printed

    Returns:
        No return

    Raises:
        TypeError: if size is not an integer number


    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for m in range(size):
        print("#" * size)
