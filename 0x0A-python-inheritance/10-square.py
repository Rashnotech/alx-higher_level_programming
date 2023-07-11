#!/usr/bin/python3

""" a square class """


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ A class that inherit the properties of base class (Rectangle) """
    def __init__(self, size):
        self.__size = size
        super().integer_validator("size", self.__size)
        super().__init__(self.__size, self.__size)

    def area(self):
        """ a method that find the area of a square """
        return self.__size ** 2
