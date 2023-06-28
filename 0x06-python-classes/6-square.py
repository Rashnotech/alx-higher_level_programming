#!/usr/bin/python3
"""
    Square: a class to calculate the shape of a square
"""


class Square:
    """ A Square with a constructor that initialize and validate
        size as of a type integer assign to a private attribute size.

        Attributes:
            __size: an integer variable declared as a private attribute
            __position: a tuple declared as private attribute
            counter: a public attribute counter
    """
    counter = 0

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """ Get the value of an attribute size """
        return self.__size

    @property
    def position(self):
        """ a class property the get position attribute """
        return self.__position

    @position.setter
    def position(self, value):
        """ a method that set position attribute """
        if len(value) != 2 or not all(isinstance(num, int) for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif int(value[0]) < 0 and int(value[1]) < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

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

    def my_print(self):
        """
            A method that prints the output of the computation
        """
        if self.__size == 0:
            print()
        else:
            if Square.counter == 1:
                print()
            for _ in range(self.__size):
                if self.__position[0] > 0:
                    for i in range(self.__position[0]):
                        if self.__position[1] > 0 and i == 0:
                            print(' ', end='')
                        elif self.__position[1] > 0:
                            print('', end='')
                        else:
                            print(' ', end='')
                for _ in range(self.__size):
                    print('#', end='')
                print()
            Square.counter += 1
