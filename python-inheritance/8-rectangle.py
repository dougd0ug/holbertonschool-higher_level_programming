#!/usr/bin/python3
"""
8-rectangle.py
Create a class BaseGeometry
"""


class BaseGeometry:
    """
    Create a class BaseGeometry
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer" .format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0" .format(name))
        elif self.height <= 0:
            raise ValueError("{} must be greater than 0" .format(self.height))
        elif self.width <= 0:
            raise ValueError("{} must be greater than 0" .format(self.width))
