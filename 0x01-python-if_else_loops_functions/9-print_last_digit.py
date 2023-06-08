#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = number * -1
    new_num = number % 10
    print("{}".format(new_num), end='')
    return new_num
