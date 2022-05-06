#!/usr/bin/python3

if __name == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 5
    b = 10
    print(f"{a} + {b} = {add(5, 10)}")
    print(f"{a} - {b} = {sub(5, 10)}")
    print(f"{a} * {b} = {mul(5, 10)}")
    print(f"{a} / {b} = {div(5, 10)}")
