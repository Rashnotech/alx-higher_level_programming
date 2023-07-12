#!/usr/bin/python3

""" a module that return JSON """


import json


def to_json_string(my_obj):
    """
        A function that returns JSON representation of an object
        Args:
            my_obj: class object
        Returns:
            JSON representation
    """
    return json.dumps(my_obj)
