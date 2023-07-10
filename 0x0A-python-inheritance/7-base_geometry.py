#!/usr/bin/python3

""" a BaseGeometry class """


class BaseGeometry:
    """ A base geometry class
        Raises:
            TypeError if not an integer
    """
    def area(self):
        """ A function that raises an Exception message """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ an integer validator """
        if not isinstance(value, int):
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
