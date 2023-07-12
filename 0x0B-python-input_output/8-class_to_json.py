#!/usr/bin/python3

""" a module that returns the dictionary description """


import json


def class_to_json(obj):
    """
        a function that converts a simple data structure to simple
        dictionary (list, dictionary, string, integer and boolean
        Args:
            obj: an instance of a class

        Return:
            dictionary description of python data structure
    """
    if isinstance(obj, (list, tuple)):
        return [class_to_json(item) for attr in obj]
    elif isinstance(obj, dict):
        return {str(key): class_to_json(value) for key, value in obj.item()}
    elif isinstance(obj, (str, int, bool)):
        return obj
    elif hasattr(obj, '__dict__'):
        return (obj.__dict__)
    else:
        return str(obj)
