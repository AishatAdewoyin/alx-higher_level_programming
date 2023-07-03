#!/usr/bin/python3

def raise_exception():
    try:
        raise TypeError("An intentional type exception has been raised.")
    except TypeError as te:
        raise te
