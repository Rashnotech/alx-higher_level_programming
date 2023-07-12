#!/usr/bin/python3

""" a module that writes an object to a text file """


import json


def save_to_json_file(my_obj, filename):
    """
        A function that writes an object to a text file
        using JSON representation
        Args:
            my_obj: python object datastructure
            filename: name of the file to write in
    """
    with open(filename, 'w') as file:
        file.write(json.dumps(my_obj))
