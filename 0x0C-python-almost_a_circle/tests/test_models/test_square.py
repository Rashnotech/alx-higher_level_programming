#!/usr/bin/python3

""" a test module for square class """


import unittest
from unittest.mock import MagicMock
from models.square import Square
from models.square import Rectangle
from models.base import Base

class TestSquare(unittest.TestCase):
    """ a test cases for Square class """

    def test_raises(self):
        """ test square if it's raises exceptions """
        s = Square(5)
        self.assertIsNotNone(s.id)
        # Test valueError
        with self.assertRaises(TypeError):
            s.size = "9"
        with self.assertRaises(TypeError):
            s.size = (3, 2)
        with self.assertRaises(ValueError):
            s.size = 0
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            s.size = "9"
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            s.size = (3, 2)
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            s.size = 0
        with self.assertRaisesRegex(ValueError, 'x must be >= 0'):
            s.x = -3
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            s.x = (3, 0)
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            s.y = {'s': 3}
        with self.assertRaisesRegex(ValueError, 'y must be >= 0'):
            s.y = -1

    def test_areas(self):
        """ test area of the square """
        s_mock = MagicMock(size=5)
        s_mock.area.return_value = s_mock.size ** 2
        s_class = Square(5)
        self.assertEqual(s_mock.area(), s_class.area())

    def test_updates(self):
        """ test update in attributes """
        s_class = Square(6, 5, 3, 5)
        s1_class = Square(6, 5, 12, 5)
        s_class.update(1, 2, 3, 4)
        s1_class.update(size=7, id=89, y=1)
        self.assertEqual(str(s_class), '[Square] (1) 3/4 - 2')
        self.assertEqual(str(s1_class), '[Square] (89) 5/1 - 7')
    
    def test_inheritance(self):
        """ Check if it inherit Rectangle or base class """
        s = Square(4)
        self.assertIsInstance(s, Rectangle)
        self.assertIsInstance(s, Base)

if __name__ == '__main__':
    unittest.main()
