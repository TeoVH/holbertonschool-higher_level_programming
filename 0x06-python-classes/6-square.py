#!/usr/bin/python3

"""
6. Coordinates of a square
Class square with Private instance attribute: position
"""


class Square:
    """
    Class Square
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes square
        """
        self.__size = size
        self.__position = position

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

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
            for i in range(self.__position[1]):
                print()
            for j in range(self.__size):
                print("{}{}".format(" " * self.position[0], "#" * self.__size))
