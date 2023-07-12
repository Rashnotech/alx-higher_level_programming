#!/usr/bin/python3

""" a module that retrieve dictionary representation """


class Student:
    """
        A function that retrieves a dictionary representation
        Attributes:
            firstname: first name of the student
            last_name: last name of the student
            age: age of the student
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
