#!/usr/bin/python3
"""writing Objects to files
"""
import json


def save_to_json_file(my_obj, filename):
    """add Object in JSON representation to a file

    Args:
        my_obj (object) - Python object
        filename (str) - file to add JSON reprentation
    """
    with open(filename, mode='w', encoding='UTF-8') as file:
        file.write(json.dumps(my_obj))
