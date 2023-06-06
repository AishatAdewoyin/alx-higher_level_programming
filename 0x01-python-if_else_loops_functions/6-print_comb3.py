#!/usr/bin/python3
for no1 in range(10):
    for no2 in range(no1 + 1, 10):
        print("{:d}{:d}".format(no1, no2), end=", " if no1 < 8 or no2 < 9 else "\n")
