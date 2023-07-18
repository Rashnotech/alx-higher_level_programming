#!/usr/bin/python3

""" a test module for square class """


import unittest
from unittest.mock import MagicMock
from models.square import Square


class TestSquare(unittest.TestCase):
    """ a test cases for Square class """

    def test_raises(self):
        """ test square if it's raises exceptions """
        s = Square(5)
        # Test valueError
        with self.assertRaises(TypeError):
            s.size = "9"
        with self.assertRaises(TypeError):
            s.size = (3, 2)

    def test_areas(self):
        """ test area of the square """
        s_mock = MagicMock(size=5)
        s_mock.area.return_value = s_mock.size ** 2
        s_class = Square(5)
        self.assertEqual(s_mock.area(), s_class.area())


if __name__ == '__main__':
    unittest.main()
