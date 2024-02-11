#!/usr/bin/python3
"""unit test for class User"""

import unittest
from models import user
import datetime

class UserTest(unittest.TestCase):
    """test cases"""

    def test_type(self):
        """instance of the class"""
        instance = user.User()
        self.assertIsInstance(instance.id, str)
        self.assertIsInstance(instance.created_at, datetime.datetime)
        self.assertIsInstance(instance.updated_at, datetime.datetime)




if __name__ == "__main__":
    unittest.main()
