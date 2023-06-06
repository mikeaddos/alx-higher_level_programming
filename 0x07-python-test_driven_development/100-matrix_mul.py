#!/usr/bin/python3
"""

this module is  a function that multiplies 2 matrices

"""


def matrix_mul(m_a, m_b):
    """ function that multiplies 2 matrices

    Args:
        m_a: matrix a
        m_b: matrix b

    Returns:
        result of  multiplication

    Raises:
        TypeError: if m_a or m_b aren't a list
        TypeError: if m_a or m_b aren't a list of a lists
        ValueError: if m_a or m_b are empty
        TypeError: if the lists of m_a or m_b don't have integers or floats
        TypeError: if the rows of m_a or m_b don't have the same size
        ValueError: if m_a and m_b can't be multiplied


    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    for elem in m_a:
        if not isinstance(elem, list):
            raise TypeError("m_a must be a list of lists")

    for elem in m_b:
        if not isinstance(elem, list):
            raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")

    for lists in m_a:
        for elem in lists:
            if not type(elem) in (int, float):
                raise TypeError("m_a should contain only integers or floats")

    for lists in m_b:
        for elem in lists:
            if not type(elem) in (int, float):
                raise TypeError("m_b should contain only integers or floats")

    length = 0

    for elem in m_a:
        if length != 0 and length != len(elem):
            raise TypeError("each row of m_a must be of the same size")
        length = len(elem)

    length = 0

    for elem in m_b:
        if length != 0 and length != len(elem):
            raise TypeError("each row of m_b must be of the same size")
        length = len(elem)

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    rw1 = []
    in1 = 0

    for a in m_a:
        rw2 = []
        in2 = 0
        number = 0
        while (in2 < len(m_b[0])):
            number += a[in1] * m_b[in1][in2]
            if in1 == len(m_b) - 1:
                in1 = 0
                in2 += 1
                rw2.append(number)
                number = 0
            else:
                in1 += 1
        rw1.append(rw2)

    return rw1
