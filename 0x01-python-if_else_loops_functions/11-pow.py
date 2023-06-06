#!/usr/bin/python3
def pow(a, b):
    ans = 1
    for _ in range(b):
        ans *= a
    return ans
