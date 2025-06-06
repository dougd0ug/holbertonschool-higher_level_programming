#!/usr/bin/env python3
'''
task_00_basic_serialization.py
'''

import json


def serialize_and_save_to_file(data, filename):
    """
    serialize to JSON standards and save it to a file
    """
    with open(filename, 'w', encoding='UTF-8') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    load and deserialize from a filename
    """
    with open(filename, 'r') as f:
        return json.load(f)
