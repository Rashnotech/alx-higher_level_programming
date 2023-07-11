#!/usr/bin/python3

""" a square class """


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ a square class that inherit integer_validator from child class """
    def __init__(self, size):
        self.__size = size
        super().integer_validator("size", size)

    def area(self):
        """ a method that calculate the area of a square """
        return self.__size ** 2

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
