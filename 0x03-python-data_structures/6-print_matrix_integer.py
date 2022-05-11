#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j in i:
            if j != i[len(i) - 1]:
                print(f"{j}", end=" ")
            else:
                print(f"{j}", end="")
        print("$")
