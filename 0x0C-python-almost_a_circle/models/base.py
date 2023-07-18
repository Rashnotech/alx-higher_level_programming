#!/usr/bin/python3

""" a base class """


import json
import os
import turtle


class Base:
    """
        a base with private attributes
        Attr:
            nb_object: number of object
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ a method that returns JSON string representation """
        if list_dictionaries == [] or list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ a method that write JSON string to a file """
        file_name = cls.__name__ + '.json'
        instance = []
        if list_objs == [] or list_objs is None:
            content = "[]"
        else:
            for ins in list_objs:
                instance.append(ins.to_dictionary())
                content = cls.to_json_string(instance)
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(content)

    @staticmethod
    def from_json_string(json_string):
        """  a method that returns the list of the JSON
            string representation
        """
        if json_string == [] or json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ a method that returns an instance with all attributes set """
        if dictionary and dictionary != {}:
            if cls.__name__ == 'Rectangle':
                instance = cls(1, 2)
            else:
                instance = cls(1)
            instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """ a method that return a list of instances """
        file_name = cls.__name__ + '.json'
        content = []
        if os.path.isfile(file_name):
            with open(file_name, 'r') as file:
                load = file.read()
            items = cls.from_json_string(load)
            for item in items:
                content.append(cls.create(**item))
            return content
        else:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ a method that write json into a csv file """
        class_name = cls.__name__ + '.csv'
        instance = []
        content = ''
        if len(list_objs) == 0 or list_objs is None:
            content = []
        else:
            for ins in list_objs:
                if not isinstance(ins, Base):
                    return
                else:
                    instance.append(ins.to_dictionary())
                    content = cls.to_json_string(instance)
        with open(class_name, 'w') as file:
            file.write(content)

    @classmethod
    def load_from_file_csv(cls):
        """ a method that return a list of instances """
        file_name = cls.__name__ + '.csv'
        content = []
        if os.path.isfile(file_name):
            with open(file_name, 'r') as file:
                load = file.read()
            items = cls.from_json_string(load)
            for item in items:
                content.append(cls.create(**item))
            return content
        else:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ a method that draws all Rectangle and Squares """
        tk = turtle.Turtle()
        tk.screen.bgcolor("#b7312c")
        tk.shape("turtle")
        tk.pensize(2)

        tk.color('#ff0000')
        for r in list_rectangles:
            tk.showturtle()
            tk.up()
            tk.goto(r.x, r.y)
            tk.down()
            for _ in range(2):
                tk.fd(r.width)
                tk.left(90)
                tk.fd(r.height)
                tk.lef(90)
            tk.hideturtle()
        tk.color('#b5e3d7')
        for s in list_squares:
            tk.showturtle()
            tk.up()
            tk.goto(s.x, s.y)
            tk.down()
            for _ in range(2):
                tk.fd(s.width)
                tk.left(90)
                tk.fd(s.height)
                tk.left(90)
            tk.hideturtle()
        tk.exitonclick()
