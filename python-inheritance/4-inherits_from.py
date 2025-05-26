#!/usr/bin/python3
"""
4-inherits_from.py
Write a function that returns True if the object is an instance of
a class that inherited (directly or indirectly)
from the specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """
    Return true is the obj is equal to a_class
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
