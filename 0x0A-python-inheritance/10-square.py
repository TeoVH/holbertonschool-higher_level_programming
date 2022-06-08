#!/usr/bin/python3
"""
10. Square #1
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
        super().__init__(size, size)
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        """
        Functions that returns the rectangle area
        """
        return (self.__size ** 2)
