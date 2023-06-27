#!/usr/bin/python3
class Square:
    """ A Square with a constructor that initialize size to
        but make sure it's a value and of type integer
        a private attribute size.
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
