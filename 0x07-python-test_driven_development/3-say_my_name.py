#!/usr/bin/python3
"""
    A function that prints first_name and last_name
    Exception:
        raised TypeError if first or last_name is not string
"""


def say_my_name(first_name, last_name=""):
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    elif not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    else:
        print('My name is {} {}'.format(first_name, last_name))
