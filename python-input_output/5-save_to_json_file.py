#!/usr/bin/python3
"""
5-save_to_json_file.py
writes an Object to a text file, using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """
    writes an Object to a text file, using a JSON representation
    """
    with open(filename, 'w', encoding="utf-8") as f:
        finil = json.dumps(my_obj)
        return f.write(finil)
