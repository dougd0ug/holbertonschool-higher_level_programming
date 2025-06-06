#!/usr/bin/env python3
'''
task_01_pickle.py
'''

import pickle


class CustomObject:
    """
    class CustomObject
    """
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def __str__(self):
        print("Name: {}" .format(self.name))
        print("Age: {}" .format(self.age))
        print("Is Student: {}" .format(self.is_student))

    def serialize(self, filename):
        return pickle.dump(filename)

    @classmethod
    def deserialize(cls, filename):
        return pickle.load(filename)
