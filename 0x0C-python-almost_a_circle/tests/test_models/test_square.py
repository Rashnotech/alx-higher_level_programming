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
            s_size = (3, 2)

    def display(size):
        output = ''
        for _ in range(size):
            output += '#' * size + '\n'
        return output

    def test_areas(self):
        """ test area of the square """
        s_mock = MagicMock(size=5)
        s_mock.area.return_value = s_mock.size ** 2
        s_class = Square(5)
        self.assertEqual(s_mock.area(), s_class.area())

    def test_display(self):
        """ test display area"""
        s_mock = MagicMock(size=2)
        s_class = Square(5)
        s_mock.display.return_value = display(s_mock.size)
        self.assertEqual(s_mock.display(), s_class.display())
        s_class = Square(5)
        self.assertEqual(str(s_class), '[Square] (1) 0/0 - 5')

    def display_cord(width, height, x, y):
        output = ''
        if y > 0:
            output += '\n' + '#' * y
        for _ in range(height):
            if x > 0:
                output += ' ' * x
                output += '#' * width + '\n'
        return output



if __name__ == '__main__':
    unittest.main()
