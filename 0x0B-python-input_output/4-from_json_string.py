#!/usr/bin/python3

""" a module that return JSON to string """


import json


def from_json_string(my_str):
    """
        A function that convert json to string
        Args:
            my_str: Json notation
        Returns:
            an object represented by a JSON string
    """
    return json.loads(my_str)
