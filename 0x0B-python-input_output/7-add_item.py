#!/usr/bin/python3
"""adds arguements to a Python list then
saves it to a file
"""
from os import path
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if path.exists('add_item.json'):
    obj_json_file = load_from_json_file('add_item.json')
else:
    obj_json_file = []

for i in range(1, len(sys.argv)):
    obj_json_file.append(sys.argv[i])

save_to_json_file(obj_json_file, 'add_item.json')
