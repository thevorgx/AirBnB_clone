#!/usr/bin/python3
"""unit test for class Review"""

import unittest
from models import review
import datetime

class ReviewTest(unittest.TestCase):
    """test cases"""

    def test_type(self):
        """test type of instance atributes"""
        instance = review.Review()
        self.assertIsInstance(instance.id, str)
        self.assertIsInstance(instance.created_at, datetime.datetime)
        self.assertIsInstance(instance.updated_at, datetime.datetime)
        self.assertIsInstance(instance.place_id, str)
        self.assertIsInstance(instance.user_id, str)
        self.assertIsInstance(instance.text, str)

    def test_default(self):
        """test default instance of the class"""
        instance = review.Review()
        self.assertEqual(instance.place_id, "")
        self.assertEqual(instance.user_id, "")
        self.assertEqual(instance.text, "")

    def test_attr_method(self):
        """test put values of instance atributes"""
        instance = review.Review()
        instance.place_id = "1234567890"
        instance.user_id = "user123"
        instance.text = "This is a review of the place."
        self.assertEqual(instance.place_id, "1234567890")
        self.assertEqual(instance.user_id, "user123")
        self.assertEqual(instance.text, "This is a review of the place.")

    def test_class(self):
        """test instance"""
        instance = review.Review()
        self.assertIsInstance(instance, review.Review)



if __name__ == "__main__":
    unittest.main()
