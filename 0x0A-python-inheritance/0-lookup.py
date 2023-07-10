#!/usr/bin/python3

""" A lookup module"""


def lookup(obj):
    """ A function that returns the list of available attributes
        and methods of an object.
    """
    return dir(obj)
