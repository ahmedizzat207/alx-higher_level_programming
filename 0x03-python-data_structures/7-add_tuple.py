#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    while (len(tuple_a) < 2):
        tuple_a += (0),
    while (len(tuple_b) < 2):
        tuple_b += (0),
    i = 0
    new_tuple = ()
    while (i < 2):
        sumtuple = tuple_a[i] + tuple_b[i]
        new_tuple += (sumtuple),
        i += 1
    return new_tuple
