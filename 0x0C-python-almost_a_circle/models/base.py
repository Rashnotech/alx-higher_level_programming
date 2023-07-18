#!/usr/bin/python3

""" a base class """


import json
import os


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
        if not isinstance(list_dictionaries, list):
            return
        elif len(list_dictionaries) == 0:
            return []
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ a method that write JSON string to a file """
        class_name = cls.__name__ + '.json'
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

    @staticmethod
    def from_json_string(json_string):
        """  a method that returns the list of the JSON
            string representation
        """
        if len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ a method that returns an instance with all attributes set """
        if len(dictionary) == 0:
            return
        if cls.__name__ == 'Rectangle':
            instance = cls(dictionary['width'], dictionary['height'])
        else:
            instance = cls(dictionary.get('width'), dictionary['x'],
                           dictionary['y'], dictionary['id'])
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
