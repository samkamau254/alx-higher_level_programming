#!/usr/bin/python3
"""This is 1-rectangle.
    It defines a rectangle.
"""


class Rectangle:
    """This defines a class Rectangle with private instances of height
    and width.
    """

    def __init__(self, width=0, height=0):
        """This initializes the width and height of the rectangle

        Arguementss:
            width (int, optional): describes the width of rectangle.
            Defaults to 0.
            height (int, optional): defines the height of rectangle.
            Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """gets the width of the rectangle

        Returns:
            int: rectangle's width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width of the rectangle.

        Args:
            value (int): the width to be checked

        Raises:
            TypeError: raised if value is not an integer
            ValueError: raised if value is < 0
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """gets the height of the rectangle

        Returns:
            int: the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """sets the value for the height of the rectangle

        Args:
            value (int): value to be set as height

        Raises:
            TypeError: raised if value is not an integer
            ValueError: raised if value < 0.
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value
