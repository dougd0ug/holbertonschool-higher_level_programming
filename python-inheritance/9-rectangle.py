#!/usr/bin/python3
"""
9-rectangle.py
Create a class Rectangle
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Create a class Rectangle
    """
    def __init__(self, width, height):
        self.integer_validator("height", height)
        self.integer_validator("width", width)
        self.__width = width
        self.__height = height

    def area(self):
        result = self.__height * self.__width
        return result

    def __str__(self):
        return ("[Rectangle] {}/{}" .format(self.__width, self.__height))
