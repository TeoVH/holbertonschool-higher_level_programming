#!/usr/bin/python3
"""
Class Rectangle: class Rectangle that inherits from Base
"""
from models.base import Base


class Rectangle(Base):
    """
    class Rectangle inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize Rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        return (self.__width * self.__height)

    def display(self):
        print("\n" * self.y +
              (" " * self.x + "#" * self.width + "\n") * self.__height, end="")

    def __str__(self):
        msg = "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)
        return(msg)

    def update(self, *args, **kwargs):
        if args:
            for i, j in enumerate(args):
                if i == 0:
                    self.id = j
                if i == 1:
                    self.__width = j
                if i == 2:
                    self.__height = j
                if i == 3:
                    self.__x = j
                if i == 4:
                    self.__y = j
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.__width = kwargs["width"]
            if "height" in kwargs:
                self.__height = kwargs["height"]
            if "x" in kwargs:
                self.__x = kwargs["x"]
            if "y" in kwargs:
                self.__y = kwargs["y"]
