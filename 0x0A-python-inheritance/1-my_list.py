#!/usr/bin/python3
"""1-my_list
"""


class MyList(list):
    """
    inherits capabilities of populating a list and prints
    it
    """
    def print_sorted(self):
        """print a list in sorted order"""
        if issubclass(MyList, List):
            print(sorted(self))
