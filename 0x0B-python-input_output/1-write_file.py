#!/usr/bin/python3
"""
Function that writes a string to a text file (UTF8)
and returns the number of characters written
"""


def write_file(filename="", text=""):
    """
    Funtion that writes in a file
    """
    with open(filename, mode="w", encoding="utf-8") as w_file:
        return(w_file.write(text))
