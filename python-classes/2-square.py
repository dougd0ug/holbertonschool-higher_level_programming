#!/usr/bin/python3
"""
2-square.py
Write an class Square that define a square
"""


class Square:
    """
    Class Square
    """
    size = None

    def __init__(self, size=0):
        """
        def the arguments
        """
        self.size = size
        if size < 0:
            raise ValueError("size must be >= 0")
        elif not isinstance(size, int):
            raise TypeError("size must be an integer")
