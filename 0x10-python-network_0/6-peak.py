#!/usr/bin/python3
"""Function to find a peak in an unsorted list of integers."""


def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.
    """
    if not list_of_integers:
        return None

    low = 0
    high = len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            high = mid
        else:
            low = mid + 1

    return list_of_integers[low]
