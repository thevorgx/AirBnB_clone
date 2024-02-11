#!/usr/bin/python3
"""unit test for class amenity"""


import unittest
from models import amenity
import datetime


class AmenityTest(unittest.TestCase):
    """test cases class State"""

    def test_type(self):
        """test type of instance atributes"""
        instance = amenity.Amenity()
        self.assertIsInstance(instance.id, str)
        self.assertIsInstance(instance.created_at, datetime.datetime)
        self.assertIsInstance(instance.updated_at, datetime.datetime)
        self.assertIsInstance(instance.name, str)

    def test_default(self):
        """test default instance of the class"""
        instance = amenity.Amenity()
        self.assertEqual(instance.name, "")

    def test_attr_method(self):
        """test put values of instance atributes"""
        instance = amenity.Amenity()
        instance.name = "John"
        self.assertEqual(instance.name, "John")

    def test_class(self):
        """test instance"""
        instance = amenity.Amenity()
        self.assertIsInstance(instance, amenity.Amenity)


if __name__ == "__main__":
    unittest.main()
