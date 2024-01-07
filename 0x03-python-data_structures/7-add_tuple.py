#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_b) == 0:
        return tuple_a
    elif len(tuple_a) < 2:
        tuple_a = (tuple_a[0], 0)
    elif len(tuple_b) < 2:
        tuple_b = (tuple_b[0], 0)
    
    new_list = [] 
    for i in range(2):
        new_list.append(tuple_a[i] + tuple_b[i])

    return tuple(new_list)
