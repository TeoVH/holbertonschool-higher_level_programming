#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    if matrix is not None:
        new_list = list()
        for i in matrix:
            new_list.append(list(map(lambda x: x**2, matrix[i])))
        return (new_list)
    return None
