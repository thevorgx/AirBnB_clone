#!/usr/bin/python3
"""unittest cases for base_model module"""


import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid

class Base_Model_Test(unittest.TestCase):
    """Base_Model_Test class (unittests for the base_model)"""

    def test_no_arg_Initialization(self):
        """test if the initializations attributes are done correctly"""

        instance = BaseModel()
        uuid_string = instance.id
        uuid_object = uuid.UUID(uuid_string)
        self.assertIsInstance(uuid_object, uuid.UUID)
        self.assertIsInstance(instance.id, str)
        self.assertIsInstance(instance.created_at, datetime)
        self.assertIsInstance(instance.updated_at, datetime)

    def test_str_method(self):
        """test __str__ method"""

        instance = BaseModel()
        instance.id = '0ba07990-9b34-41c8-a9cf-fed53f7cd400'
        instance.created_at = datetime(2024, 2, 11, 16, 14, 47, 15113)
        instance.updated_at = datetime(2024, 2, 11, 16, 14, 47, 15171)
        instance.name = 'My First Model'
        instance.my_number = 89

        my_str = instance.__str__()
        expected_output = "[BaseModel] (0ba07990-9b34-41c8-a9cf-fed53f7cd400) {'id': '0ba07990-9b34-41c8-a9cf-fed53f7cd400', 'created_at': datetime.datetime(2024, 2, 11, 16, 14, 47, 15113), 'updated_at': datetime.datetime(2024, 2, 11, 16, 14, 47, 15171), 'name': 'My First Model', 'my_number': 89}"

        self.assertEqual(my_str, expected_output)

    def test_save_method(self):
        """test the save method"""

        instance = BaseModel()
        original_updated_at = instance.updated_at

        instance.save()
        new_updated_at = instance.updated_at

        self.assertNotEqual(new_updated_at, original_updated_at)


if __name__ == "__main__":
    unittest.main()
