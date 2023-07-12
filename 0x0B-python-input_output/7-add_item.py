#!/usr/bin/python3

""" a module that add all arguments to pylist """


import sys
import os.path


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

args = sys.argv
filename = 'add_item.json'
items = []
if len(args) == 1:
    if os.path.isfile(filename):
        load = load_from_json_file(filename)
        load.extend(items)
        save_to_json_file(load, filename)
    else:
        save_to_json_file(items, filename)
else:
    for wrd in args[1:]:
        items.append(wrd)
    load = load_from_json_file(filename)
    load.extend(items)
    save_to_json_file(load, filename)
