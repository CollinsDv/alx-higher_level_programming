#!/usr/bin/python3
def uniq_add(my_list=[]):
    # remove duplicates
    new_set = set(my_list)

    total = 0
    # loop set to access items
    for num in new_set:
        total += num

    return total
