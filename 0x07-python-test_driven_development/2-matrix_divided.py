#!/usr/bin/python3
"""
1. Divide a matrix
Function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Returns a new matrix
    """
    tye = "matrix must be a matrix (list of lists) of integers/floats"
    if len(matrix) == 0:
        raise TypeError(tye)
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for i in matrix:
        if len(i) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        if len(i) == 0 or type(i) is not list:
            raise TypeError(tye)
        new_list = []
        for j in i:
            if type(j) not in (int, float):
                raise TypeError(tye)
            new_list.append(round(j/div, 2))
        new_matrix.append(new_list)
    return new_matrix
