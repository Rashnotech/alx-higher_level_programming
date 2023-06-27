#!/usr/bin/python3
"""
    Square: a class to calculate the shape of a square
"""


class Square:
    """ A Square with a constructor that initialize and validate
        size as of a type integer assign to a private attribute size.

        Attributes:
            size: an integer variable to take an integer value
    """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """ Get the value of an attribute size """
        return self.__size

    @size.setter
    def size(self, size=0):
        """ A setter function for size """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ A method that finds the area of a square using a
            private attribute.
        """
        return self.__size ** 2
