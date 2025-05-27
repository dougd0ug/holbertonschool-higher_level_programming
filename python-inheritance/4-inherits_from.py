#!/usr/bin/python3
"""
4-inherits_from.py
Write a function that returns True if the object is an instance of
a class that inherited (directly or indirectly)
"""


def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a class that inherited
    (directly or indirectly), otherwise false
    """
    if isinstance(obj, a_class):
        if type(obj) is not a_class:
            return (True)
        else:
            return (False)
    else:
        return (False)
