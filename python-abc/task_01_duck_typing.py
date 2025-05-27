#!/usr/bin/python3
"""
Create an abc class
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    ABC Animal class
    """
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """
    Dog class inherit from Animal
    """
    def sound(self):
        return "Bark"


class Cat(Animal):
    """
    Cat class inherit from Animal
    """
    def sound(self):
        return "Meow"
