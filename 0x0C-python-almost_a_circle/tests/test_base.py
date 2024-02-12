import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def setUp(self):
        self.ob1 = Base()
        self.ob2 = Base()
        self.ob3 = Base(30)
        self.ob4 = Base()

    def tearDown(self):
        Base._Base__nb_objects = 0

    """null input"""
    def test_null_input(self):
        self.assertEqual(self.ob1.id, 1)

    """multiple null classes"""
    def test_input(self):
        self.assertEqual(self.ob3.id, 30)
