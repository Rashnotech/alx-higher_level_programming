#!/usr/bin/python3

""" a Base Geometry class """


class BaseGeometry:
    """ A BaseGeometry class with non implemented area method
        Raises:
            NotImplemented
    """

    def area(self):
        """ a method that raise an exception """
        raise Exception('area() is not implemented')
