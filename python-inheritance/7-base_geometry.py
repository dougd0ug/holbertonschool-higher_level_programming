#!/usr/bin/python3
"""
7-base_geometry.py
Create a class BaseGeometry
"""


class BaseGeometry:
    """
    Create a class BaseGeometry
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer" .format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0" .format(name))
