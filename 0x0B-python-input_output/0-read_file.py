#!/usr/bin/python3
"""
Function that reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """
    Funtion to read the file
    """
    with open(filename, mode="r", encoding="utf-8") as p_file:
        print(p_file.read(), end="")
