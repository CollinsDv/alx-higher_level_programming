#!/usr/bin/python3
"""
module determining class instances
"""


def is_kind_of_class(obj, a_class):
    """
    Return True if obj is instance of a class,
    of if it's an instance of a class inherited
    from a specified class
    otherwise False

    Args:
        obj - Object of interest
        a_class - aledged inherited class

    """
    if isinstance(obj, a_class):
        return True
    
    return False
