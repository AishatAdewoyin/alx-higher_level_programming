#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        tuple_fix = (0, "None")
    else:
        tuple_fix = (len(sentence), sentence[0])
    return tuple_fix
