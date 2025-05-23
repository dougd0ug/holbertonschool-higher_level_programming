#!/usr/bin/python3
"""
2-square.py
Write an class Square that define a square
"""


class Square:
    """
    Class Square
    """
    def __init__(self, size=0):
        """
        def the arguments
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
