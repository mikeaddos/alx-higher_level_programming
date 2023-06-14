#!/usr/bin/python3
"""function that defines a Pascal's Triangle function"""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n

    Returns a list of lists of integers representing the triangle
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        temp = [1]
        for m in range(len(tri) - 1):
            temp.append(tri[m] + tri[m + 1])
        temp.append(1)
        triangles.append(temp)
    return triangles
