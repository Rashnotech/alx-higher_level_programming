#!/usr/bin/python3

"""
    MagicClass: a magic class that can find the area and circumference

"""


class MagicClass:
    """
        MagicClass: a class that validates the radius data types
            before (__init__) before initializing the protected
            attribute

        Attibutes:
            _MagicClass: a protected attribute that stores the radius of
            a circle
    """

    def __init__(self, radius):
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        else:
            self.__radius = radius

    def area(self):
        """ A method that find the area of a circle """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """ A method that find the circumference of a circle """
        return self.__radius * 2 * math.pi
