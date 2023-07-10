#!/usr/bin/python3

""" A module that return True if an instance is true """


def is_same_class(obj, a_class):
    if type(obj) is a_class:
        return True
    else:
        return False
