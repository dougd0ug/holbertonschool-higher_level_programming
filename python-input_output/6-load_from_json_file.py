#!/usr/bin/python3
"""
5-load_from_json_file.py
writes an Object to a text file, using a JSON representation
"""
import json


def load_from_json_file(filename):
    """
    writes an Object to a text file, using a JSON representation
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
