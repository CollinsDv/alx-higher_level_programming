#!/usr/bin/python3
"""adds arguements to a Python list then
saves it to a file
"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

argc = len(sys.argv)

filename = 'add_item.json'
my_list = []
try:
    my_list = load_from_json_file(filename)
except BaseException:
    pass
for items in range(1, argc):
    my_list.append(argv[items])
save_to_json_file(my_list, filename)
