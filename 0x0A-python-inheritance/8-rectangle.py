#!/usr/bin/python3

""" a rectangle class that inherit another class"""


class Rectangle(BaseGeometry):
    """ a class that inherits from BaseGeometry class """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

        super().integer_validator("width", self.__width)
        super().integer_validator("height", self.__height)
