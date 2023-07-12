#!/usr/bin/python3
"""
This module contains the class MyInt
"""


class MyInt(int):
    """Class myInt!"""
    def __new__(cls, *args, **kwargs):
        """create a new instance of the class"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """equal to magic method"""
        return int(self) != other

    def __ne__(self, other):
        """not equal to magic method"""
        return int(self) == other
