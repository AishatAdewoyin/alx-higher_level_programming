#!/usr/bin/python3
def no_c(my_string):
    a_string = ''.join(char for char in my_string if char.lower() != 'c')
    return a_string
