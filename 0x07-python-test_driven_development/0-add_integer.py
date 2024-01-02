#!/usr/bin/python3

"""This module is called 0-add_integer.
Arguements used:
  a: first int to be added.
  b: second int to be added.
"""

def add_integer(a, b=98):
    """This function adds 2 integers or floats that are
    first casted to integers, otherwise TypeError is raised.
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError('a must be an integer')
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError('b must be an integer')
    a = int(a)
    b = int(b)
    return a + b
