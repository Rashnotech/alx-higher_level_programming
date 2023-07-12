#!/usr/bin/python3

""" a script that add that add all arguments to a python list """


import sys
import os.path


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

args = sys.argv
filename = 'add_item.json'
items = []


def file_exist(filename, content):
    """
        A function that checks if a filename already exist before
        loading from json and adding to file
        Args:
            filename: name of the file to load and save to
            content: content to write into a file
    """
    load = load_from_json_file(filename)
    load.extend(content)
    save_to_json_file(load, filename)


if len(args) == 1:
    if os.path.isfile(filename):
        file_exist(filename, items)
    else:
        save_to_json_file(items, filename)
else:
    for wrd in args[1:]:
        items.append(wrd)
    if os.path.isfile(filename):
        file_exist(filename, items)
    else:
        save_to_json_file(items, filename)
