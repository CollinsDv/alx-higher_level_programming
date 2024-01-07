#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    # reverse the list
    my_list.reverse()

    # display the items line by line
    for item in my_list:
        print("{:d}".format(item))
