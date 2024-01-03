#!/usr/bin/python3
"""4-print_square, a function that prints a square
using the '#' symbol depending on its size
"""

def print_square(size):
    """The funcion print_square prints a square depending
    on size

    Arguements:
        size (int): length and width of the square

    Raises:
        TypeError: if size is not an integer
        ValueError: if size less than 0
        TypeError: if size is float and less than 0
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if isinstance(size, float) and size <= 0:
        raise TypeError('size must be an integer')
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
