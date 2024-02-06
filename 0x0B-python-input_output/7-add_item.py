#!/usr/bin/python3
"""adds arguements to a Python list then
saves it to a file
"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = 'file.json'
List = []

try:
    List = load_from_json_file(filename)
except BaseException:
    pass

List.extend(sys.argv[1:])

save_to_json_file(List, filename)
