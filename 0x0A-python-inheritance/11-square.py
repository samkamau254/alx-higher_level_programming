#!/usr/bin/python3
"""This module contains the class Square that inherits
BaseGeometry
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square that inherits BaseGeometry

    Args:
        BaseGeometry (class): Parent class
    """

    def __init__(self, size):
        """Instantiation with size

        Args:
            size (int): square's size
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """Returns area of square

        Returns:
            int: area of square
        """
        return self.__size * self.__size

    def __str__(self):
        """Method that returns the printable string
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
