#!/usr/bin/python3
"""
    Square: a class to calculate the shape of a square
"""


class Square:
    __result = 0
    """ A Square with a constructor that initialize and validate
        size as of a type integer assign to a private attribute size.

        Attributes:
            __size: an integer variable to take an integer value
            __result: a private attribute declared as a private method
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
        self.__result = self.__size ** 2
        return self.__result
    
    def my_print(self):
        """
            A method that prints the output of the computation
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for x in range(self.__result):
                    print('{}'.format('#', end=""))
                print()
