#!/usr/bin/python3
"""
Function that writes an Object to a text file, using a JSON representation
"""


from json import dumps


def save_to_json_file(my_obj, filename):
    """
    Function that writes the object
    """
    with open(filename, mode="w") as w_file:
        w_file.write(dumps(my_obj))
