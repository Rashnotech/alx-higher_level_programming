#!/usr/bin/python3

""" A module that checks if an object is an instance of a class """


def inherits_from(obj, a_class):
    """ A function that checks if an object is an instance of a class
        that inherits a specified class.
        Return:
            True otherwise false
    """
    if not type(obj) is a_class or not isinstance(obj, a_class):
        return True
    else:
        return False
