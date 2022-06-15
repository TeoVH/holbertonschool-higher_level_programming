#!/usr/bin/python3
"""Class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter"""
        self.width = value
        self.height = value

    def __str__(self):
        """Str method"""
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.size))

    def update(self, *args, **kwargs):
        """Update the class by adding the public method
        that assigns attributes"""
        if len(args):
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.size = arg
                if i == 2:
                    self.x = arg
                if i == 3:
                    self.y = arg

        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
