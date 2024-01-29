#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """tests all edge cases"""
    def test_none(self):
        # Arrange
        List = None
        # Assert
        # self.assertRaises(TypeError, max_integer, List)
        with self.assertRaises(TypeError):
            max_integer(List)

    def test_empty_list(self):
        # Act
        result = max_integer()
        # Assert
        self.assertEqual(result, None)

    def test_sorted(self):
        # Act
        result = max_integer([1, 2, 3, 4])
        # Assert
        self.assertEqual(result, 4)

    def test_unsorted(self):
        self.assertEqual(max_integer([1, 2, 4, 3]), 4)

    def test_negative(self):
        self.assertEqual(max_integer([-10, -100, -23]), -10)

if __name__ == "__main__":
    unittest.main()
