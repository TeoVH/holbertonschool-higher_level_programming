#!/usr/bin/python3

"""
4. Access and update private attribute
Update the private attribute __size
"""


class Square:
    """
    Class Square

    Functions:
        __init__(self, size=0):
        size(self):
        size(self, value):
        area(self):
    """
    def __init__(self, size=0):
        """
        Initializes square
        """
        self.size = size

    @property
    def size(self):
        """
        Return: size
        """
        return self.__size

    @property setter
    def size(self, value):
        """
        Setter

        value: if size >= 0 sets size to value
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
        Returns: the square area
        """
        return (self.__size) ** 2
