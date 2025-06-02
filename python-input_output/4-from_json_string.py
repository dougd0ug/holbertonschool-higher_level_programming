#!/usr/bin/python3
"""
3-to_json_string.py
returns the JSON representation of an object
"""
import json


def from_json_string(my_str):
    """
     returns an object (Python data structure) represented by a JSON string
    """
    return json.dump(my_str)
