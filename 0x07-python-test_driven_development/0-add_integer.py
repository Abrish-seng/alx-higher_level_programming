#!/usr/bin/python3

def add_integer(a, b=98):
    """Add two integers"""
    if type(a) not in [int, float]:
        raise TypeError("a must be and integer")
    if type(b) not in [int,float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
