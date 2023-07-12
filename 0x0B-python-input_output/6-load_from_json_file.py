#!/usr/bin/python3

""" a module that creates an object """


import json


def load_from_json_file(filename):
    """
        A function that creates an object from a JSON file
        Args:
            filename: file that contain JSON
    """
    with open(filename) as file:
        obj = json.load(file)
    return obj
