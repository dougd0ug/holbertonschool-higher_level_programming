#!/usr/bin/python3
"""
910-square.py
Create a class Square
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Create a class Square
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        result = self.__size * self.__size
        return result
