#!/usr/bin/python3
"""
This module contains a function that appends a string
"""


def append_write(filename="", text=""):
    """A function that appends a string ate the end of a text
    file and returns number of Characters.

    args:
        filename: name of file apppending to
        text: String to be added.

    returns:
        Number of characters added"""
    with open(filename, 'a', encoding='utf=8') as newfile:
        return newfile.write(text)
