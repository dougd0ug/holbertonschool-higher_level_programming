#!/usr/bin/python3
"""
1-write_file.py
Read a file
"""


def write_file(filename="", text=""):
    """
    Function for read a file
    """
    with open(filename, encoding="utf-8") as f:
        f.write(text)
