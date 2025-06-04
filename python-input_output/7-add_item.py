#!/usr/bin/python3
"""
7-add_item.py
adds all arguments to a Python list, and then save them to a file
"""


import json
import os
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

if os.path.exists(filename):
    try:
        my_list = load_from_json_file(filename)
    except Exception:
        my_list = []
else:
    my_list = []

new_items = sys.argv[1:]
for item in new_items:
    my_list.append(item)

save_to_json_file(my_list, filename)
