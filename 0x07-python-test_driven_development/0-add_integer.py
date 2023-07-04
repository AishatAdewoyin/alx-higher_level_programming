#!/usr/bin/python3
"""the function module that adds up 2 different integers"""


def add_integer(a, b=98):
    """Returns the sum of two integers or two different floats as int.
    Args:
    - a: the first passed argument
    - b: the second passed argument
    Raises:
    - TypeError: In case either of the arguments is not an int or a float
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
