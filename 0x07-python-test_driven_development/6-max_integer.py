#!/usr/bin/python3
"""
the module to find the maximum int in the list
"""


def max_integer(list=[]):
    """the function that finds and return max int in a list of integers
        If list is empty it returns None
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
