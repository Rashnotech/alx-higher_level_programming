#!/usr/bin/python3

""" Unit Test file """


import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from unittest.mock import MagicMock


class TestBase(unittest.TestCase):
    """ Few test case on base class """

    test_suite = [1, 12, 12.4, [2, 3, 4, 5], {'x': 2, 'y': 3}, (4, 5)]
    def test_instance(self):
        """ a test_case that manage id attribute call
            to avoid id duplication
        """
        base_mock = MagicMock()
        base_mock.id = 1
        base_class = Base(1)
        self.assertEqual(base_mock.id, base_class.id)

    def test_assignment(self):
        """ a test_case that checked the assigned value to
            id attribute
        """
        for test in self.test_suite:
            base_mock = MagicMock(id=test)
            base_class = Base(test)
            self.assertEqual(base_mock.id, base_class.id)

    def test_to_json_string(self):
        """ a testcase that check if a json is return """
        r1 = Rectangle(10, 7, 2, 8, 1)
        dictionary = r1.to_dictionary()
        json_dict = Base.to_json_string([dictionary])
        json_none = Base.to_json_string([])
        self.assertIsNotNone(json_dict)
        self.assertEqual(json_none, "[]")

    def test_save_to_file(self):
        """ a testcase that check if file is written """
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        s1 = Square(5, 3, 4, 2)
        s2 = Square(3)
        Rectangle.save_to_file([r1, r2])
        Square.save_to_file([])
        self.assertTrue(os.path.isfile('Rectangle.json'))
        self.assertTrue(os.path.isfile('Square.json'))
        with open('Rectangle.json', 'r') as f:
            f.read()
        with open('Square.json', 'r') as fs:
            fs.read()
        self.assertIsNotNone(f)
        self.assertIsNotNone(fs)

    def test_from_json_string(self):
        """ a testcase that check from json_string """
        test_suite = [
                {'id': 89, 'width': 10, 'height': 4},
                {'id': 7, 'width': 1, 'height': 7}
                ]
        json_input = Rectangle.to_json_string(test_suite)
        output = Rectangle.from_json_string(json_input)
        r1 = Rectangle.from_json_string(None)
        self.assertEqual(output, test_suite)
        self.assertEqual(r1, [])

    def test_create(self):
        """ test create method """
        r1 = Rectangle(3, 5, 1, 0, 1)
        dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**dictionary)
        self.assertEqual(str(r1), '[Rectangle] (1) 1/0 - 3/5')
        self.assertEqual(str(r2), '[Rectangle] (1) 1/0 - 3/5')
        self.assertIsNot(r1, r2)
        self.assertFalse(r1 == r2)



if __name__ == '__main__':
    unittest.main()
