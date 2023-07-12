#!/usr/bin/python3
"""
This module contains the json str function
"""

import json


def from_json_string(my_str):
    """returns an object represented by a JSON string
    args:
        my_str: string parameter"""
    return json.loads(my_str)
