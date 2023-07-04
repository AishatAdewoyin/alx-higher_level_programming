#!/usr/bin/python3
"""
This module contains a function that adds two integers or floats.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats and returns their sum.

    Args:
        a: An integer or float value to be added.
        b: An integer or float value to be added (default value is 98).

    Returns:
        An integer representing the sum of a and b.

    Raises:
        TypeError: If a or b is not of integer or float type.
    """
    # Check if a is either an integer or a float
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")

    # Check if b is either an integer or a float
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")

    # Convert a and b to integers if they are floats
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    # Add the integers a and b
    result = a + b

    # Return the sum of a and b
    return result
