#!/usr/bin/python3
def safe_function(fct, *args):
    from sys import stderr
    try:
        result = fct(*args)
    except Exception as i:
        stderr.write("Exception: {}\n".format(i))
        result = None
    return (result)
