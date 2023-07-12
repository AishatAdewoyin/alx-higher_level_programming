#!/usr/bin/python3
"""
This module contains
a function that creates an Object from a JSON file.
"""

import json


def load_from_json_file(filename):
    """creates an object from a JSON file
    args:
        filename: the file"""
    with open(filename, 'r', encoding='utf-8') as newfile:
        return json.load(newfile)
