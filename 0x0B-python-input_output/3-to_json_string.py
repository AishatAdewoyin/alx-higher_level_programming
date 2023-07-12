#!/usr/bin/python3
"""
This module contains the JSON Representation
of object string
"""

import json


def to_json_string(my_obj):
    """returns the JSON representation of an object (string)

    args:
        my_obj: The object String"""
    return json.dumps(my_obj)
