#!/usr/bin/python3
"""
9. Full rectangle
Class Rectangle
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class Rectangle

    Attributes:
        __width
        __height
    """
    def __init__(self, width, height):
        """
        Initializes rectangle
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """
        Functions that returns the rectangle area
        """
        return (self.__height * self.__width)

    def __str__(self):
        """
        Function that returns a description
        """
        x = "[Rectangle]" + " " + str(self.__width) + "/" + str(self.__height)
        return (x)
