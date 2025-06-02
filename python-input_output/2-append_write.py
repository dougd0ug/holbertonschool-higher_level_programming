#!/usr/bin/python3
"""
1-write_file.py
Read a file
"""


def append_write(filename="", text=""):
    """
    fonction to append a string in a file
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
