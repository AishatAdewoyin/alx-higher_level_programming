#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_m = tuple_a + (0, 0)
    tuple_n = tuple_b + (0, 0)
    tuple_fix = (tuple_m[0] + tuple_n[0], tuple_m[1] + tuple_n[1])
    return tuple_fix
