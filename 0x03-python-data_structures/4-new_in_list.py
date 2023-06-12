#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return (my_list)
    else:
        fix_list = my_list.copy()
        fix_list[idx] = element
        return (fix_list)
