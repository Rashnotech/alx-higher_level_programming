#!/usr/bin/python3

""" a function that add attribute """


def add_attribute(obj, attr_name, attr_value):
    """ a function that adds a new attribute to an object
        Raise:
            TypeError if attribute can't be added
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    else:
        obj.__dict__[attr_name] = attr_value
