#!/usr/bin/python3
"""
Create an abc class
"""


class SwimMixin:
    """
    ABC SwimMixin
    """
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """
    ABC FlyMixin
    """
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Mixing class inherits SwimMixin and FlyMixin
    """
    def roar(self):
        print("The dragon roars!")
