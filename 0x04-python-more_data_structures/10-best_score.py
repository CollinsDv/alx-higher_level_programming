#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return
    # sort the dict in reverse order
    tup = sorted(a_dictionary.items(), reverse=True)
    #change 1st tuple element to list and obtain the name
    return list(tup[0])[0]
