#!/usr/bin/python3
"""Python object conversion
"""
import json


def to_json_string(my_obj):
    """return Python object from JSON string

    Args:
        my_obj (obj) - JSON
    Return:
        Python object
    """
    return json.loads(my_obj)
