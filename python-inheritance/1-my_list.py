#!/usr/bin/python3
"""
1-ly_list.py
Write a class MyList that inherits from list
"""


class MyList(list):
    """
    class inherit from list
    """
    def print_sorted(self):
        """
        Print a sorted list
        """
        print(sorted(self))
