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
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        elif value <= 0:
            raise ValueError("<name> must be greater than 0")
