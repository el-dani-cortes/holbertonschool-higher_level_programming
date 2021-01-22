#!/usr/bin/python3
"""Unittest for base.py file
"""
import unittest
from models.base import Base


class Test_Base(unittest.TestCase):
    """Defines a class to evaluate diferent test cases for base.py file"""

    def test_instance_class(self):
        """Checks for a instance of the class"""
        b1 = Base(3)
        self.assertIsInstance(b1, Base)

    def test_none_id(self):
        """Checks when id is none"""

        b1 = Base()
        self.assertEqual(b1.id, 1)

        b1 = Base()
        self.assertEqual(b1.id, 2)

        b1 = Base()
        self.assertEqual(b1.id, 3)

    def test_id_value(self):
        """Checks when id has a value"""

        b1 = Base(12)
        self.assertEqual(b1.id, 12)

        b1 = Base(-4)
        self.assertEqual(b1.id, -4)

        b1 = Base(0)
        self.assertEqual(b1.id, 0)

        b1 = Base(100e+1000)
        self.assertEqual(b1.id, 100e+1000)
