#!/usr/bin/python3
"""
This module contains the write_file function
"""


def write_file(filename="", text=""):
    """This function returns the number of Character written to filename"""
    with open(filename, 'w', encoding='utf=8') as newfile:
        return newfile.write(text)
