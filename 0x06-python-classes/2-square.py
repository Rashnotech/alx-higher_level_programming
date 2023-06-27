#!/usr/bin/python3
"""
    Square: A class to find the square of a number
"""


class Square:
    """ A Square with a constructor that initialize size
    """
    def __init__(self, size=0):
        """
            A constructor that validate and initialize size to
            a private attribute size
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
