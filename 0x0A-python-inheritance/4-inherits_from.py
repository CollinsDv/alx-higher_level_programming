#!/usr/bin/python3
"""
module determining types and class instances
"""


def inherits_from(obj, a_class):
    """
    Return True if obj is an instance of a class that inherited
    from a specified class, otherwise False

    Args:
        obj - Object of interest
        a_class - aledged inherited class

    """
    if issubclass(obj, a_class):
        return True

    return False
