#!/usr/bin/python3
"""
5-text_indentation.py
prints a text with 2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters: ., ? and :
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    buffer = ""

    for char in text:
        buffer += char
        if char in ".?:":
            print(buffer.strip())
            print()
            buffer = ""

    if buffer.strip():
        print(buffer.strip())
