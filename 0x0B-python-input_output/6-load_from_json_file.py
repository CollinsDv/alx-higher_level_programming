#!/usr/bin/python3
"""generating Object from JSON file
"""
import json


def load_from_json_file(filename):
    """convert to a python object from a JSON file contents

    Args:
        filename (str) - file to obtain JSON reprentation
    """
    with open(filename, mode='r', encoding='UTF-8') as file:
        return json.load(file)
