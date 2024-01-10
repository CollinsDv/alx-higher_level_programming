#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # sort the dict and store them in a variable as a tuple
    tup = sorted(a_dictionary.items())
    # print the pair items in a loop
    for key, value in tup:
        print("{}: {}".format(key, value))
