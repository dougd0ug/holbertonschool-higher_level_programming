#!/usr/bin/python3
"""
Create an abc class
"""


class Fish:
    """
    ABC Fish class
    """
    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")


class Bird:
    """
    ABG Bird class
    """
    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    Flying Fish inherits Fish and Bird
    """
    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")
