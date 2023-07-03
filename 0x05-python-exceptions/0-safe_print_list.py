#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    list_count = 0
    try:
        for i in range(x):
            print(f"{my_list[i]}", end="")
            list_count += 1
    except IndexError:
        pass
    finally:
        print()
    return list_count
