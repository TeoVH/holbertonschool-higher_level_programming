#!/usr/bin/python3


def uppercase(str):
    for i in str:
        c = ord(i)
        if c <= 122 and c >= 97:
            print(f"{chr(c - 32)}", end="")
        else:
            print(f"{chr(c)}", end="")
        print()
