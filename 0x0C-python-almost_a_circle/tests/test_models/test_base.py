#!/usr/bin/python3

""" Unit Test file """


import unittest
from models.base import Base
from unittest.mock import MagicMock


class TestBase(unittest.TestCase):
    """ Few test case on base class """

    test_suite = [None, 12, 12.4, [2, 3, 4, 5], {'x': 2, 'y': 3}, (4, 5)]
    def test_instance(self):
        """ a test_case that manage id attribute call
            to avoid id duplication
        """
        for _ in range(4):
            base_mock = MagicMock()
            base_class = Base()
            self.assertEqual(base_mock.id, base_class.id)

    def test_assignment(self):
        """ a test_case that checked the assigned value to
            id attribute
        """
        for test in self.test_suite:
            base_mock = MagicMock(return_value=test)
            base_class = Base(test)
            self.assertEqual(base_mock.id, base_class.id)


if __name__ == '__main__':
    unittest.main()
