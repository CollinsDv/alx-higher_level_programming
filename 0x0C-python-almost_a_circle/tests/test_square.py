#!/usr/bin/python3
import unittest
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base
import json


class TestSquare(unittest.TestCase):
    def setUp(self):
        self.s1 = Square(5, 5, 2)
        self.s2 = Square(2, 2, 1)

    def tearDown(self):
        Square.reset()

    def test_correct_input(self):
        self.assertEqual(self.s1.size, 5)
        self.assertEqual(self.s2.size, 2)

    def test_missing_inputs(self):
        with self.assertRaises(TypeError):
            s1 = Square()

    def test_negative(self):
        with self.assertRaises(ValueError):
            s3 = Square(-10, -20)
        with self.assertRaises(ValueError):
            s4 = Square(20, -120)
        with self.assertRaises(ValueError):
            s5 = Square(-20, 120)

    def test_extra_values(self):
        with self.assertRaises(TypeError):
            s6 = Square(10, 23, 21, 31, 32, 23)

    def test_string_input(self):
        with self.assertRaises(TypeError):
            s1 = Square('cake', 'tea')

    def test_list(self):
        with self.assertRaises(TypeError):
            s1 = Square([10, 20])

    def test_area(self):
        self.assertEqual(self.s1.area(), 25)
        self.assertEqual(self.s2.area(), 4)

    def test_display(self):
        self.assertEqual(self.s1.display(), None)
        self.assertEqual(self.s2.display(), None)

    def test_str_dunder(self):
        self.assertEqual(self.s1.__str__(), '[Square] (1) 5/2 - 5')
        self.assertEqual(self.s2.__str__(), '[Square] (2) 2/1 - 2')

    def test_args_update(self):
        self.s1.update(89, 2, 3, 4)

        self.assertEqual(self.s1.id, 89)
        self.assertEqual(self.s1.size, 2)
        self.assertEqual(self.s1.x, 3)
        self.assertEqual(self.s1.y, 4)

    def test_args_kwargs(self):
        self.s1.update(x=1, size=2, y=3, width=4)

        self.assertEqual(self.s1.id, 1)
        self.assertEqual(self.s1.x, 1)
        self.assertEqual(self.s1.y, 3)
        self.assertEqual(self.s1.size, 2)

    def test_setter_getter(self):
        self.assertEqual(self.s1.width, 5)
        self.assertEqual(self.s1.height, 5)

    def test_save_to_file(self):
        Square.save_to_file(None)
        with open('Square.json', 'r', encoding='UTF-8') as f:
            self.assertEqual('[]', f.read())

    def test_class(self):
        self.assertTrue(str(Square), "<class 'models.square.Square'>")


    def test_save_load_file(self):
        s1 = Square(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Square.save_to_file([s1, r2])
        load_file = Square.load_from_file()
        self.assertTrue(isinstance(load_file, list))

    def test_to_dict(self):
        dict1 = self.s1.to_dictionary()
        self.assertEqual({'id': 1, 'size': 5, 'x': 5, 'y': 2}, dict1)
        self.assertTrue(isinstance(dict1, dict))

    def test_square(self):
        self.assertTrue(issubclass(Square, Base))
