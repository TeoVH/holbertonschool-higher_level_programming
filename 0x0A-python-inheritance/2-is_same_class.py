#!/usr/bin/python3
"""
2. Exact same object
Function that returns True if the object is exactly an instance
of the specified class otherwise False
"""


def is_same_class(obj, a_class):
    """
    Function that returns True or False
    """
    if type(obj) is a_class:
        return True
    if type(obj) is not a_class:
        return False
