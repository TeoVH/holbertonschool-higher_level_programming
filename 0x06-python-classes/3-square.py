#!/usr/bin/python3

"""
3. Area of a square
Class Square with public instance method that returns the current square area
"""


class Square:
    """Class Square"""
    def __init__(self, size=0):
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

    def area(self):
        """
        Calculates area of square
        Returns the square area
        """
        return (self.__size) ** 2
