#!/usr/bin/python3

"""
2. Size validation
Defines class Square with private attribute and size validation
"""


class Square:
    """Class Square"""
    def __init__(self, size):
        """
        Initializes square

        __size: Private instance attribute;
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
