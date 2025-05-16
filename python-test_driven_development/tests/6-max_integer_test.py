#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_one_element(self):
        self.assertEqual(max_integer([42]), 42)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -5, -3]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-10, 0, 10]), 10)

    def test_floats(self):
        self.assertEqual(max_integer([1.2, 3.4, 2.5]), 3.4)

    def test_mixed_int_and_float(self):
        self.assertEqual(max_integer([1, 2.2, 3]), 3)

    def test_all_equal(self):
        self.assertEqual(max_integer([2, 2, 2]), 2)

    def test_string_input(self):
        self.assertEqual(max_integer("abcd"), "d")

    def test_list_of_strings(self):
        self.assertEqual(max_integer(["abc", "b", "cde"]), "cde")

    def test_none_input(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_list_with_none(self):
        with self.assertRaises(TypeError):
            max_integer([1, None, 3])

    def test_list_with_mixed_types(self):
        with self.assertRaises(TypeError):
            max_integer([1, "2", 3])
