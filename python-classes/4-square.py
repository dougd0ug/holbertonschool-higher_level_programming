#!/usr/bin/python3
"""
4-square.py
Write an class Square that define a square
"""


class Square:
    """
    Class Square
    """
    def __init__(self, size=0):
        """
        def the arguments and conditions of initialisation
        """
        self.__size = size

    @property
    def size(self):
        """
        def the property
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        def the setter
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        return the area of a square
        """
        area_square = self.__size * self.__size
        return area_square
