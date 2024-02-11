#!/usr/bin/python3
"""unit test for class Place"""

import unittest
from models import place
import datetime

class PlaceTest(unittest.TestCase):
    """test cases"""

    def test_type(self):
        """test type of instance atributes"""
        instance = place.Place()
        self.assertIsInstance(instance.id, str)
        self.assertIsInstance(instance.created_at, datetime.datetime)
        self.assertIsInstance(instance.updated_at, datetime.datetime)
        self.assertIsInstance(instance.city_id, str)
        self.assertIsInstance(instance.user_id, str)
        self.assertIsInstance(instance.name, str)
        self.assertIsInstance(instance.description, str)
        self.assertIsInstance(instance.number_rooms, int)
        self.assertIsInstance(instance.number_bathrooms, int)
        self.assertIsInstance(instance.max_guest, int)
        self.assertIsInstance(instance.price_by_night, int)
        self.assertIsInstance(instance.latitude, float)
        self.assertIsInstance(instance.longitude, float)
        self.assertIsInstance(instance.amenity_ids, list)

    def test_default(self):
        """test default instance of the class"""
        instance = place.Place()
        self.assertEqual(instance.city_id, "")
        self.assertEqual(instance.user_id, "")
        self.assertEqual(instance.name, "")
        self.assertEqual(instance.description, "")
        self.assertEqual(instance.number_rooms, 0)
        self.assertEqual(instance.number_bathrooms, 0)
        self.assertEqual(instance.max_guest, 0)
        self.assertEqual(instance.price_by_night, 0)
        self.assertEqual(instance.latitude, 0.0)
        self.assertEqual(instance.longitude, 0.0)
        self.assertEqual(instance.amenity_ids, [])

    def test_attr_method(self):
        """test put values of instance atributes"""
        instance = place.Place()
        instance.city_id = "123456789"
        instance.user_id = "user123"
        instance.name = "Cozy Apartment"
        instance.description = "comfortable apartment"
        instance.number_rooms = 2
        instance.number_bathrooms = 3
        instance.max_guest = 4
        instance.price_by_night = 100
        instance.latitude = 37.7749
        instance.longitude = 122.4194
        instance.amenity_ids = [1, 2, 3]
        self.assertEqual(instance.city_id, "123456789")
        self.assertEqual(instance.user_id, "user123")
        self.assertEqual(instance.name, "Cozy Apartment")
        self.assertEqual(instance.description, "comfortable apartment")
        self.assertEqual(instance.number_rooms, 2)
        self.assertEqual(instance.number_bathrooms, 3)
        self.assertEqual(instance.max_guest, 4)
        self.assertEqual(instance.price_by_night, 100)
        self.assertEqual(instance.latitude, 37.7749)
        self.assertEqual(instance.longitude, 122.4194)
        self.assertEqual(instance.amenity_ids, [1, 2, 3])

    def test_class(self):
        """test instance"""
        instance = place.Place()
        self.assertIsInstance(instance, place.Place)






if __name__ == "__main__":
    unittest.main()
