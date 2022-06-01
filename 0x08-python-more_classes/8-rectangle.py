#!/usr/bin/python3
"""
8. Compare rectangles
Static method that returns the biggest rectangle based on the area
"""


class Rectangle:
    """
    Class Square

    Attributes:
        __width
        __height
        number_of_instances

    Methods:
        def area(self)
        def perimeter(self)
        def __str__(self)
        def __repr__(self)
        def __del__(sself)
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes square
        """
        self.width = width
        self.height = height
        self.__class__.number_of_instances += 1

    def __str__(self):
        """
        Returns a string with # rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return ""
        string = ""
        for i in range(0, self.__height):
            string += str(self.print_symbol) * self.__width
            if i < self.__height - 1:
                string += "\n"
        return string

    def __repr__(self):
        """
        Return a string representation of the rectangle
        """
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(self):
        """
        Destructor
        """
        print("Bye rectangle...")
        self.__class__.number_of_instances -= 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Returns the rectangle are
        """
        return (self.__height * self.__width)

    def perimeter(self):
        """
        Returns the rectangle perimeter
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return ((self.__height * 2) + (self.__width * 2))

    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() < rect_2.area():
            return rect_2
        return rect_1
