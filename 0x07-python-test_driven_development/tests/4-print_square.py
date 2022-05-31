#!/usr/bin/python3
"""
3. Print square
Function that prints a square with the character #
"""


def print_square(size):
    """
    Print a square
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(0, size):
        print("#" * size)
        i += 1
