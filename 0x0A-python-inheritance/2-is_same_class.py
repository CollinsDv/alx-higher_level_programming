#!/usr/bin/python3
"""
module determining class instances
"""


def is_same_class(obj, a_class):
    """
    Return True if obj is instance of a class,
    otherwise False

    Args:
        obj - Object of interest
        a_class - aledged inherited class

    """
    if isinstance(obj, a_class) is True:
        return True
    else:
        return False
