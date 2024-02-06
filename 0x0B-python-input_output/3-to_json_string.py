#!/usr/bin/python3
"""JSON representation of a Python object
"""
import json


def to_json_string(my_obj):
    """return JSON string of object

    Args:
        my_obj (obj) - Python object
    Return:
        JSON string
    """
    return json.dumps(my_obj)
