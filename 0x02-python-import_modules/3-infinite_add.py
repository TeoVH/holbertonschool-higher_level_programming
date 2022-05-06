#!/usr/bin/python3
from sys import argv


def main():
    resultado = 0
    if len(argv) == 1:
        resultado = 0
    else:
        for i in argv[1:]:
            resultado += int(i)
    print(f"{resultado}")


if __name__ == "__main__":
    main()
