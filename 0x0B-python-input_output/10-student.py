#!/usr/bin/python3
"""
Class Student
"""


class Student:
    """
    Class Student
    """
    def __init__(self, first_name, last_name, age):
        """
        Initialize the class
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Public method that retrieves a dictionary
        representation of a Student instance
        """
        if attrs is None:
            return self.__dict__
        dict = {}
        for i in attrs:
            if i in self.__dict__:
                dict[i] = self.__dict__[i]
        return dict
