#!/usr/bin/python3

""" a test module for rectangle class """


import unittest
from unittest.mock import MagicMock
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ a test cases for rectangle class """

    def test_inheritance(self):
        """ check if rectangle inherits base class attribute """
        # Create MagicMock instances with proper configuration
        rect_mock = MagicMock(width=10, height=2, id=1)
        rect_mock_1 = MagicMock(width=10, height=2, x=0, y=0, id=12)
        # Create Rectangle instances
        rect_class = Rectangle(10, 2)
        rect_class_1 = Rectangle(10, 2, 0, 0, 12)
        # Perform the assertions
        self.assertEqual(rect_mock.id, rect_class.id)
        self.assertEqual(rect_mock_1.id, rect_class_1.id)
        self.assertEqual(rect_mock_1.width, rect_class_1.width)
        self.assertEqual(rect_mock.height, rect_class.height)

    def test_raises(self):
        """ test rectangle if it's raises exceptions """
        test_value_error = [-2, -4, -5, -1, -13]
        test_type_error = [[2, 4], {'k': 3, 'y': 5}, 2.3, 5j, 'Hello', (3, 4)]
        r1_class = Rectangle(10, 2, 3, 3)
        # Test valueError
        for test in test_value_error:
            with self.assertRaises(ValueError):
                r1_class.width = test
            with self.assertRaises(ValueError):
                r1_class.height = test
            with self.assertRaises(ValueError):
                r1_class.x = test
            with self.assertRaises(ValueError):
                r1_class.y = test

        # Test TypeError
        for test in test_type_error:
            with self.assertRaises(TypeError):
                r1_class.width = test
            with self.assertRaises(TypeError):
                r1_class.height = test
            with self.assertRaises(TypeError):
                r1_class.x = test
            with self.assertRaises(TypeError):
                r1_class.y = test

    def display(self, width, height):
        output = ''
        for _ in range(height):
            output += '#' * width + '\n'
        return output

    def test_areas(self):
        """ test area of the rectangle """
        rect_mock = MagicMock(width=4 , height=2)
        rect_mock.area.return_value = rect_mock.width * rect_mock.height
        rect_class = Rectangle(4, 2)
        self.assertEqual(rect_mock.area(), rect_class.area())

    def test_display(self):
        """ test display area"""
        r_mock = MagicMock(width=2, height=2)
        rect_class = Rectangle(2, 2)
        r_mock.display.return_value = self.display(r_mock.width, r_mock.height)
        self.assertEqual(r_mock.display(), rect_class.display())
        rect_class = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(rect_class), '[Rectangle] (12) 2/1 - 4/6')

    def display_cord(self, width, height, x, y):
        output = ''
        if y > 0:
            output += '\n' + '#' * y
        for _ in range(height):
            if x > 0:
                output += ' ' * x
                output += '#' * width + '\n'
        return output

    def test_display_cord(self):
        """ test display coordinate """
        r_mock = MagicMock(width=2, height=3, x=2, y=2)
        r_mock.display.return_value = self.display_cord(r_mock.width, r_mock.height,
                r_mock.x, r_mock.y)
        rect_class = Rectangle(2, 3, 2, 2)
        self.assertEqual(r_mock.self.display(), str(rect_class.display()))

    def test_argument_order(self):
        """ test argument order """
        r_class = Rectangle(10, 10, 10, 10)
        r_class.update(89, 2)
        self.assertEqual(str(r_class), '[Rectangle] (89) 10/10 - 2/10')

    def test_kwargs_argument(self):
        """ test kwargs argument """
        r_mock = MagicMock(width=10, 10, 10, 10)
        r_mock.update(height=1)
        self.assertEqual(str(r_class), '[Rectangle] (1) 10/10 - 10/1')


if __name__ == '__main__':
    unittest.main()
