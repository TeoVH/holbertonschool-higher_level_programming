#!/usr/bin/python3
"""
4. Only sub class of
Function that returns True if the object is an instance of a class that
inherited from the specified class ; otherwise False
"""


def inherits_from(obj, a_class):
    """
    Funtion that returns True or False
    """
    if type(obj) is not a_class:
        return True
    if type(obj) is a_class:
        return False
