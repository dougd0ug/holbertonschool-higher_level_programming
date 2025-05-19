#!/usr/bin/python3
"""
3-square.py
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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        return the area of a square
        """
        area_square = self.__size * self.__size
        return area_square
