#!/usr/bin/python3
"""
2-is_same_class.py
Write a function that returns True if the object is exactly
an instance of the specified class ; otherwise False.
"""


def is_same_class(obj, a_class):
    """
    return True or False
    """
    return type(obj) is a_class
