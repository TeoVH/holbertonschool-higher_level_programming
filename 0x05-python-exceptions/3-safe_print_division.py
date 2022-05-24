#!/usr/bin/python3


def safe_print_division(a, b):
    try:
        division = a / b
        print("Inside result: {:.1f}".format(division))
    except (ZeroDivisionError, TypeError):
        division = None
        print("Inside result: {}".format(division))
    finally:
        return division
