#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle
from io import StringIO
from os import sys
from models.base import Base


class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.r1 = Rectangle(5, 5, 2, 2)
        self.r2 = Rectangle(2, 2, 1, 4)

    def tearDown(self):
        Rectangle.reset()

    def test_rectangle(self):
        self.assertTrue(str(Rectangle), "<class 'models.rectangle.Rectangle'>")

    def test_rectangle_inheritance(self):
        self.assertTrue(issubclass(Rectangle, Base))

    def test_correct_input(self):
        self.assertEqual(self.r1.width, 5)
        self.assertEqual(self.r1.height, 5)

        self.assertEqual(self.r2.width, 2)
        self.assertEqual(self.r2.height, 2)

    def test_missing_inputs(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle()
        with self.assertRaises(TypeError):
            r2 = Rectangle(20)

    def test_negative(self):
        with self.assertRaises(ValueError):
            r3 = Rectangle(-10, -20)
        with self.assertRaises(ValueError):
            r4 = Rectangle(20, -120)
        with self.assertRaises(ValueError):
            r5 = Rectangle(-20, 120)

    def test_extra_values(self):
        with self.assertRaises(TypeError):
            r6 = Rectangle(10, 23, 21, 31, 32, 23)

    def test_string_input(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle('cake', 'tea')

    def test_list(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle([10, 20])

    def test_area(self):
        self.assertEqual(self.r1.area(), 25)
        self.assertEqual(self.r2.area(), 4)

    def test_display(self):
        self.assertEqual(self.r1.display(), None)
        self.assertEqual(self.r2.display(), None)

    def test_str_dunder(self):
        self.assertEqual(self.r1.__str__(), '[Rectangle] (1) 2/2 - 5/5')
        self.assertEqual(self.r2.__str__(), '[Rectangle] (2) 1/4 - 2/2')

    def test_args_update(self):
        self.r1.update(89, 2, 3, 4, 5)

        self.assertEqual(self.r1.id, 89)
        self.assertEqual(self.r1.width, 2)
        self.assertEqual(self.r1.height, 3)
        self.assertEqual(self.r1.x, 4)
        self.assertEqual(self.r1.y, 5)

    def test_args_kwargs(self):
        self.r1.update(x=1, height=2, y=3, width=4)

        self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r1.width, 4)
        self.assertEqual(self.r1.height, 2)
        self.assertEqual(self.r1.x, 1)
        self.assertEqual(self.r1.y, 3)
