#!/usr/bin/python3
"""
2-square.py
Write an class Square that define a square
"""


class Square:
    """
    Class Square
    """
    __size = None

    def __init__(self, size=0):
        self.size = __size

    if __size < 0:
        raise ValueError("size must be >= 0")
    if not isinstance(int, __size):
        raise TypeError("size must be an integer")
