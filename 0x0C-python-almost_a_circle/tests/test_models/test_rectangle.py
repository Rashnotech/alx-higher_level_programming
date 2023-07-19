#!/usr/bin/python3

""" a test module for rectangle class """


import unittest
from unittest.mock import MagicMock
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square


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
        self.assertIsInstance(rect_class, Base)
        self.assertNotIsInstance(rect_class, Square)
        self.assertNotEqual(rect_mock.id, rect_class.id)
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

    def test_areas(self):
        """ test area of the rectangle """
        rect_mock = MagicMock(width=4 , height=2)
        rect_mock.area.return_value = rect_mock.width * rect_mock.height
        rect_class = Rectangle(4, 2)
        r1_class = Rectangle(8, 7, 0, 0, 12)
        r1_mock = MagicMock(width=8, height=7, x=0, y=0, id=12)
        r1_mock.area.return_value = r1_mock.width * r1_mock.height
        self.assertEqual(rect_mock.area(), rect_class.area())
        self.assertEqual(r1_mock.area(), r1_class.area())

    def test_display(self):
        """ test display area"""
        r_mock = MagicMock(width=2, height=2)
        rect_class = Rectangle(2, 2)
        rect_class = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(rect_class), '[Rectangle] (12) 2/1 - 4/6')
        self.assertNotEqual(str(rect_class), '[Rectangle] (1) 0/0 - 2/2')

    def test_argument_order(self):
        """ test argument order """
        r_class = Rectangle(10, 10, 10, 10)
        r_class.update(89, 2)
        r1_class = Rectangle(10, 10, 10, 10, 10)
        r1_class.update(89, 2, 3, 4)
        self.assertEqual(str(r_class), '[Rectangle] (89) 10/10 - 2/10')
        self.assertEqual(str(r1_class), '[Rectangle] (89) 4/10 - 2/3')

    def test_kwargs_argument(self):
        """ test kwargs argument """
        r_class = Rectangle(10, 10, 10, 10, 1)
        r1_class = Rectangle(10, 10, 10, 10, 10)
        r_class.update(height=1)
        r1_class.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r_class), '[Rectangle] (1) 10/10 - 10/1')
        self.assertEqual(str(r1_class), '[Rectangle] (89) 3/1 - 2/10')

    def test_to_dictionary(self):
        """ test to dictionary method """
        r1 = Rectangle(10, 2, 1, 9, 2)
        r2 = Rectangle(1, 1)
        dictionary = r1.to_dictionary()
        r2.update(**dictionary)
        self.assertEqual(dictionary, {'x': 1, 'y': 9, 'id': 2, 'height': 2, 'width': 10})
        self.assertEqual(str(r1), '[Rectangle] (2) 1/9 - 10/2')
        #self.assertEqual(type(dictionary), <class 'dict'>)
        self.assertEqual(str(r2), '[Rectangle] (2) 1/9 - 10/2')
        self.assertFalse(r1 == r2)


    def test_raises_message(self):
        """ test rectangle if it's raises exceptions """
        test_value_error = [-2, -4, -5, -1, -13]
        test_type_error = [[2, 4], {'k': 3, 'y': 5}, 2.3, 5j, 'Hello', (3, 4)]
        r1_class = Rectangle(10, 2, 3, 3)
        # Test valueError
        for test in test_value_error:
            with self.assertRaisesRegex(ValueError, 'width must be > 0'):
                r1_class.width = test
            with self.assertRaisesRegex(ValueError, 'height must be > 0'):
                r1_class.height = test
            with self.assertRaisesRegex(ValueError, 'x must be >= 0'):
                r1_class.x = test
            with self.assertRaisesRegex(ValueError, 'y must be >= 0'):
                r1_class.y = test

        # Test TypeError
        for test in test_type_error:
            with self.assertRaisesRegex(TypeError, 'width must be an integer'):
                r1_class.width = test
            with self.assertRaisesRegex(TypeError, 'height must be an integer'):
                r1_class.height = test
            with self.assertRaisesRegex(TypeError, 'x must be an integer'):
                r1_class.x = test
            with self.assertRaisesRegex(TypeError, 'y must be an integer'):
                r1_class.y = test

if __name__ == '__main__':
    unittest.main()
