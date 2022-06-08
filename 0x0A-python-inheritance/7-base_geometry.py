#!/usr/bin/python3
"""
7. Integer validator
Class BaseGeometry with public instance methods
"""


class BaseGeometry:
    """
    Class BaseGeometry

    Methods:
        area()
        integer_validator()
    """
    def area(self):
        """
        Function with a Exception raise message
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Function that validates value
        """
        if type(name) is not str:
            raise TypeError("name must be an integer")
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
