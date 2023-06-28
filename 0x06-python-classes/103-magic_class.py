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

    def __init__(self, radius=0):
        if not (isinstance(radius, (float, int)):
            raise TypeError('radius must be a number')
        else:
            self._MagicClass__radius = radius

    def area(self):
        """ A method that find the area of a circle """
        return self._MagicClass__radius ** 2 * math.pi

    def circumference(self):
        """ A method that find the circumference of a circle """
        return self._MagicClass__radius * 2 * math.pi
