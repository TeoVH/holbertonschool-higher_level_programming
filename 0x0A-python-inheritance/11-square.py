#!/usr/bin/python3
"""
11. Square #2
Class Square
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class Square

    Attributes:
        __size

    Methods:
        area()
    """
    def __init__(self, size):
        """
        Initializes square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Functions that returns the rectangle area
        """
        return (self.__size * self.__size)

    def __str__(self):
        """
        Function that returns a description
        """
        return ("[Square]" + " " + str(self.__size) + "/" + str(self.__size))
