#!/usr/bin/python3
"""
module of 4-print_square.py.
"""


def print_square(size):
    """
prints square with "#"'s that has length of some size

args
	size: square size
Exception Error
	TypeError: if size is !int
	ValueError: if size is < than 0.
"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size > 0:
        print(("#" * size + "\n") * size, end="")
