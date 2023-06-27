#!/usr/bin/python3
"""
    Square: A square class to find the square of an
    integer number
"""


class Square:
    """ A Square with a constructor that initialize size to
        but make sure it's a value and of type integer
        a private attribute size.
        
        Attributes:
            size: An integer operand to take in value from
            a class

    """
    def __init__(self, size=0):
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
