#!/usr/bin/python3
"""unit test for class User"""

import unittest
from models import user
import datetime

class UserTest(unittest.TestCase):
    """test cases"""

    def test_type(self):
        """test type of instance atributes"""
        instance = user.User()
        self.assertIsInstance(instance.id, str)
        self.assertIsInstance(instance.created_at, datetime.datetime)
        self.assertIsInstance(instance.updated_at, datetime.datetime)
        self.assertIsInstance(instance.email, str)
        self.assertIsInstance(instance.first_name, str)
        self.assertIsInstance(instance.last_name, str)

    def test_default(self):
        """test default instance of the class"""
        instance = user.User()
        self.assertEqual(instance.email, "")
        self.assertEqual(instance.password, "")
        self.assertEqual(instance.first_name, "")
        self.assertEqual(instance.last_name, "")

    def test_attr_method(self):
        """test put values of instance atributes"""
        instance = user.User()
        instance.email = "example@example.com"
        instance.password = "password123"
        instance.first_name = "John"
        instance.last_name = "Doe"
        self.assertEqual(instance.email, "example@example.com")
        self.assertEqual(instance.password, "password123")
        self.assertEqual(instance.first_name, "John")
        self.assertEqual(instance.last_name, "Doe")

    def test_class(self):
        """test instance"""
        instance = user.User()
        self.assertIsInstance(instance, user.User)






if __name__ == "__main__":
    unittest.main()
