#!/bin/bash/python3
def uppercase(s):
    uppercase_str = ""
    for c in s:
        if ord(c) >= 97 and ord(c) <= 122:
            c = chr(ord(c) - 32)
        uppercase_str += c
    print(uppercase_str)

uppercase("best")
uppercase("Best School 98 Battery street")
