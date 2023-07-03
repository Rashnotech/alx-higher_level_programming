#!/usr/bin/python3
""" A Rectangle class
    Attr:
        width: private attribute of Rectangle class
        height: private attribute of Rectangle class
    Raise:
        TypeError if width and height are not an integer
        ValueError if width and height  are less than zero
"""


class Rectangle:
    """ Class Module below """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """ A getter method for width """
        return self.__width

    @width.setter
    def width(self, value):
        """ A method that sets an attribute """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """ A getter method for height """
        return self.__height

    @height.setter
    def height(self, value):
        """ A method that sets an attribute """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif height < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        """ A method that find the area of a rectangle """
        return self.width * self.height

    def perimeter(self):
        """ A method that find the perimeter of a rectangle """
        return 2 * self.width + self.height

    def __str__(self):
        """ A print Rectangle class like a text """
        printout = ""
        if (self.height or self.width) == 0:
            printout = ""
        else:
            for _ in self.height:
                printout += "#" * self.width
                printout += "\n"
        return printout
    
    def __eval__(self):
        """ create a new instance """
        return Rectangle()

    def __del__(self):
        print('Bye rectangle...')