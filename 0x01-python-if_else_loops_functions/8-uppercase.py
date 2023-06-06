#!/bin/bash/python3
def uppercase(string):
    uppercase_str = ""
    for char in string:
        if 97 <= ord(char) <= 122:
            uppercase_char = chr(ord(char) - 32)
            uppercase_str += uppercase_char
        else:
            uppercase_str += char
    print("{}".format(uppercase_str))
