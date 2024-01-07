#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if not tuple_a:
        return tuple_b
    if not tuple_b:
        return tuple_a
    if len(tuple_a) < 2:
        tuple_a = (tuple_a[0], 0)
    if len(tuple_b) < 2:
        tuple_b = (tuple_b[0], 0)

    new_list = []
    for i in range(2):
        new_list.append(tuple_a[i] + tuple_b[i])

    return tuple(new_list)
