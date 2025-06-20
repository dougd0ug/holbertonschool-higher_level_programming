#!/usr/bin/python3
"""
Create an abc class
"""


class VerboseList(list):
    """
    ABC VerboseList class
    """
    def append(self, item):
        super().append(item)
        print("Added [{}] to the list." .format(item))

    def extend(self, item):
        super().extend(item)
        print("Extended the list with [{}] items." .format(len(item)))

    def remove(self, item):
        super().remove(item)
        print("Removed [{}] from the list." .format(item))

    def pop(self, item=-1):
        item = super().pop(item)
        print("Popped [{}] from the list." .format(item))
        return item
