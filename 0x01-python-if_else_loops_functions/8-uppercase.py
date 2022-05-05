#!/usr/bin/python3


def uppercase(str):
    for i in str:
        c = ord(i)
        if c <= 122 and c >= 97:
            c = c - 32
            print(f"{chr(c)}", end="")
        else:
            print(f"{chr(c)}", end="")
    print()
