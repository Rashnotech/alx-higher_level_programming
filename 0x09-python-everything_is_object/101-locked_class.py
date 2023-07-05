#!/usr/bin/python3
""" A class with no object attribute """


class LockedClass:
    """ Locked Class with no attribute """
    def __setattr__(self, name, value):
        if not hasattr(self, name) and name != 'first_name':
            raise AttributeError(f'LockedClass object has no attribute {name}')
        super().__setattr__(name, value)
