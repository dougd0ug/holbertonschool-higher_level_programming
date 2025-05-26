#!/usr/bin/python3
"""
0-lookup.py
Write a function that returns the list
of available attributes and methods of an object
"""


def lookup(obj):
    """
    Return list object
    """
    return dir(obj)
