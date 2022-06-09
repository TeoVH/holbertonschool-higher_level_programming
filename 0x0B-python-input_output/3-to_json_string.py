#!/usr/bin/python3
"""
Function that returns the JSON representation of an object (string)
"""


from json import dumps


def to_json_string(my_obj):
    """
    Function that returns the JSON
    """
    return dumps(my_obj)
