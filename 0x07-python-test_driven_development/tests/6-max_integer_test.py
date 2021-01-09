#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Defines a class to evaluate diferent test cases"""

    def test_integer_numbers(self):
        """Checks for max integer in list of integers"""
        # All positive integers
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        # All negative integers
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        # Negative and positive integers
        self.assertEqual(max_integer([-1, 2, -3, -4]), 2)
        # One integer
        self.assertEqual(max_integer([1]), 1)
        # One negative integer
        self.assertEqual(max_integer([-20]), -20)

    def test_float_numbers(self):
        """Check only float numbers"""
        # Check for a infinite number
        self.assertEqual(max_integer([1, 2, 4, 10e+1000]), 10e+1000)
        # Check all positive float numbers
        self.assertEqual(max_integer([1.0, 2.2, 4.3, 100.4]), 100.4)
        # Check all negative float numbers
        self.assertEqual(max_integer([-1.0, -2.2, -4.3, -100.4]), -1.0)

    def test_strings(self):
        """Check for strings as arguments"""
        # Check for list with a string inside
        self.assertEqual(max_integer(['daniel']), 'daniel')
        # Check for string as argument
        self.assertEqual(max_integer('daniel'), 'n')
        # Check for a list of strings
        self.assertEqual(max_integer(['daniel', 'cortes', 'sully']), 'sully')
        # Check between a upper and lower case
        self.assertEqual(max_integer(['H', 'h']), 'h')

    def test_raise_type(self):
        """Check for raises diferents TypeError"""
        self.assertRaises(TypeError, max_integer, True)
        self.assertRaises(TypeError, max_integer, ['daniel', 2, 5, 20])
        self.assertRaises(TypeError, max_integer, [2, 5, "daniel", 20])
