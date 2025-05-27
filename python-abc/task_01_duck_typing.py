#!/usr/bin/python3
"""
Create an abc class
"""

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """
    ABC shape class
    """
    @abstractmethod
    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):
    """
    Circle class inherit from Shape
    """
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return pi * self.__radius * self.__radius

    def perimeter(self):
        return 2 * pi * self.__radius


class Rectangle(Shape):
    """
    Rectangle class inherit from Shape
    """
    def __init__(self, height, width):
        self.__height = height
        self.__width = width

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        return (2 * self.__width) + (2 * self.__height)


def shape_info(shape):
    area = shape.area()
    perimeter = shape.perimeter()
    print("Area : {}" .format(area))
    print("Perimeter : {}" .format(perimeter))
