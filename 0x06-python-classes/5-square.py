#!/usr/bin/python3

"""
5. Printing a square
Public instance method that prints in stdout the square with the character #
"""


class Square:
    """
    Class Square
    """
    def __init__(self, size=0):
        """
        Initializes square
        """
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set __size to value
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculates area of square
        Returns: the square area
        """
        return (self.__size) ** 2

    def my_print(self):
        """
        print  square
        """
        if self.__size == 0:
            print("")
            return
        else:
            for i in range(0, self.__size):
                print("#" * self.__size)
