#!/usr/bin/python3

for i in range(ord('a'), ord('z')+1):
    if i != ord('e') and i != ord('q'):
        print(f"{chr(i)}", end='')
