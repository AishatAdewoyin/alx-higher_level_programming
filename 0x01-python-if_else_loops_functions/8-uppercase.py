#!/bin/bash/python3
def uppercase(s):
    for c in s:
        if ord(c) >= 97 and ord(c) <= 122:
            offset = 32
        else:
            offset = 0
        print("{}".format(chr(ord(c) - offset)), end="")
    print()
