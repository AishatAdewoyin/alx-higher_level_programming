#!/usr/bin/python3
"""
This module contains append after function
"""


def append_after(filename="", search_string="", new_string=""):
    """appends new_string after a line containing
    search_string in filename
    args:
        filename: The file to search.
        search_string: The string to searh for in filename
        new_string: The new string to append"""
    with open(filename, 'r', encoding='utf-8') as newfile:
        line_number = []
        while True:
            line = newfile.readline()
            if line == "":
                break
            line_number.append(line)
            if search_string in line:
                line_number.append(new_string)
    with open(filename, 'w', encoding='utf-8') as newfile:
        newfile.writelines(line_number)
