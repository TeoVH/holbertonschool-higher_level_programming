#!/usr/bin/python3
"""
1. My list
Class My_list with a public method that print the list sorted
"""


class MyList(list):
    """
    Class MyList that inherits from list
    """
    def print_sorted(self):
        print(sorted(self))
