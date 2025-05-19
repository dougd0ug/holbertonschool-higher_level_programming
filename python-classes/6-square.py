#!/usr/bin/python3
"""
5-square.py
Write an class Square that define a square
"""


class Square:
    """
    Class Square
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        def the arguments and conditions of initialisation
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        def the property
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        def the setter
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        def the property position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        def the setter postion
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        return the area of a square
        """
        area_square = self.__size * self.__size
        return area_square

    def my_print(self):
        if self.size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
