#!/usr/bin/python3
"""
Function that creates an Object from a “JSON file”
"""


import json


def load_from_json_file(filename):
    """
    Function that creates the object
    """
    with open(filename, mode="r") as r_file:
        return json.load(r_file)
