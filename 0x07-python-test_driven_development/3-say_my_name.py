#!/usr/bin/python3
""""the say_my_name function prints a name at a time"""


def say_my_name(first_name, last_name=""):
    '''This function prints names (<first name> <last name>)
    Args:
    - first_name (str): first name to print
    - last_name (str): last name to print
    Raises:
        TypeError: thrown if either first_name and last_name arent strings
    '''

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
