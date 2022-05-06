#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    i = 0
    longitud = len(argv)
    if (longitud - 1) == 1:
        print("{} argument:".format(longitud - 1))
        print("{}: {}".format(i + 1, argv[i + 1]))
    elif (longitud - 1) > 1:
        print("{} arguments:".format(longitud - 1))
        while i < (longitud - 1):
            print("{}: {}".format(i + 1, argv[i + 1]))
            i = i + 1
    else:
        print("{} arguments.".format(i))
