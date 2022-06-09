#!/usr/bin/python3
"""
Function that returns a list of lists of integers
representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """
    Function that returns the Pascal’s triangle of n
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for p in range(1, n):
        i = [1]
        for t in range(1, p):
            i.append(triangle[p-1][t-1] + triangle[p-1][t])
        i.append(1)
        triangle.append(i)
    return triangle
