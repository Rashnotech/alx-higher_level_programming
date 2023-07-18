#!/usr/bin/python3

""" a module that inherits id attribute from the base class """


from .base import Base


class Rectangle(Base):
    """ a Rectangle class that can get and set it's method
        Raises:
            TypeError: if attributes not an integer
            ValueError: if attributes is less or equal to zero
        Attr:
            width: width of the Rectangle
            height: height of the Rectangle
            x: the x coordinate
            y: the y coordinate
            id: an indentify
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ a method that get the value of width """
        return self.__width

    @width.setter
    def width(self, width):
        """ a method that sets the value of a private attribute width """
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        elif width <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = width

    @property
    def height(self):
        """ a method that get the value of height """
        return self.__height

    @height.setter
    def height(self, height):
        """ a method that sets the value of a private attribute height """
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        elif height <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = height

    @property
    def x(self):
        """ a method that get the value of x coordinates """
        return self.__x

    @x.setter
    def x(self, x):
        """ a method that sets the value of a
            private attribute coordinate x
        """
        if not isinstance(x, int):
            raise TypeError('x must be an integer')
        elif x < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = x

    @property
    def y(self):
        """ a method that gets the value of y coordinates """
        return self.__y

    @y.setter
    def y(self, y):
        """ a method that sets the value of a private
            attribute coordinate y
        """
        if not isinstance(y, int):
            raise TypeError('y must be an integer')
        elif y < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = y

    def area(self):
        """ a method that calculate the area of a Rectangle """
        return self.height * self.width

    def display(self):
        """ a method that illustrate the computed area of a rectangle """
        print('\n' * self.y, end='')
        for _ in range(self.height):
            print(' ' * self.x, end='')
            print(self.width * '#')

    def __str__(self):
        """ a method that returns Rectangle class attributes """
        return("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width,
                                                       self.height))

    def update(self, *args, **kwargs):
        """ a method that assigns an argument to each attribute """
        size = len(args)
        if size > 0:
            attributes = ['id', 'width', 'height', 'x', 'y']
            for attr, value in zip(attributes, args):
                setattr(self, attr, value)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
                else:
                    pass

    def to_dictionary(self):
        """ a method that returns a dictionary representation
            of a rectangle
        """
        class_name = self.__class__.__name__
        attrs = self.__dict__
        return {key.replace(f"_{class_name}__", ""): value for key,
                value in attrs.items()}
