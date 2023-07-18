#!/usr/bin/python3

""" a module that handles all about square """


from .rectangle import Rectangle


class Square(Rectangle):
    """ a square clas with attributes
        Attr:
            size: size of the angle
            x: x coordinate
            y: y coordinate
        Raise:
            TypeError inherited from rectangle class
            ValueError inherited from rectangle class
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ a method that gets the value of size """
        return self.width

    @size.setter
    def size(self, size):
        """ a method that sets the value of a private attribute size """
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """ a method that update all the attribute in the class """
        attrs = ['id', 'size', 'x', 'y']
        if len(args) != 0:
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """ a method that return dictonary representation of square """
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}

    def __str__(self):
        """ returns details of square attributes """
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                  self.y, self.width))
