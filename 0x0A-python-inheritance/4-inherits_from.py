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
    if isinstance(obj, a_class) \
       and issubclass(a_class, obj.__class__) is False:
        return True

    return False
