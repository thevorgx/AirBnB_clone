#!/usr/bin/python3
"""unit test for class City"""


import unittest
from models import city
import datetime


class CityTest(unittest.TestCase):
    """test cases class State"""

    def test_type(self):
        """test type of instance atributes"""
        instance = city.City()
        self.assertIsInstance(instance.id, str)
        self.assertIsInstance(instance.created_at, datetime.datetime)
        self.assertIsInstance(instance.updated_at, datetime.datetime)
        self.assertIsInstance(instance.name, str)
        self.assertIsInstance(instance.state_id, str)

    def test_default(self):
        """test default instance of the class"""
        instance = city.City()
        self.assertEqual(instance.name, "")

    def test_attr_method(self):
        """test put values of instance atributes"""
        instance = city.City()
        instance.name = "John"
        instance.state_id = "CA"
        self.assertEqual(instance.name, "John")
        self.assertEqual(instance.state_id, "CA")

    def test_class(self):
        """test instance"""
        instance = city.City()
        self.assertIsInstance(instance, city.City)


if __name__ == "__main__":
    unittest.main()
