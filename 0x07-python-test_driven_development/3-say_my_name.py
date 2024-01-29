#!/usr/bin/python3

"""
Module: 3-say_my_name.py
Function: say_my_name
Args: first_name (str)
      last_name (str)
"""


def say_my_name(first_name, last_name=""):
    """print a formatted name"""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
