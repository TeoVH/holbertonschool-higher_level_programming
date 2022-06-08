#!/usr/bin/python3
"""
Class BaseGeometry with public methods
"""


class BaseGeometry:
    """
    class BaseGeometry
    """

    def area(self):
        """
        raises an Exception message
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        public method
        """
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
