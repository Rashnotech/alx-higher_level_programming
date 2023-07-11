#!/usr/bin/python3

""" A module that checks if an object is an instance of a class """


def inherits_from(obj, a_class):
    """ A function that checks if an object is an instance of a class
        that inherits a specified class.
        Return:
            True otherwise false
    """
    return type(obj) is not a_class and issubclass(type(obj), a_class)
