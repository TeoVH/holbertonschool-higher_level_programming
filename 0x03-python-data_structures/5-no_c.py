#!/usr/bin/python3


def no_c(my_string):
    for i in my_string:
        new_str = ""
        if i != 'c' and i != 'C':
            new_str += i

    return new_str
