#!/usr/bin/python3
"""
Create an abc class
"""


class CountedIterator:
    """
    ABC CountedIterator class
    """
    def __init__(self, obj):
        self.iterator = iter(obj)
        self.counter = 0

    def get_count(self):
        return self.counter

    def __next__(self):
        try:
            item = next(self.iterator)
            self.counter += 1
            return item
        except StopIteration:
            raise
