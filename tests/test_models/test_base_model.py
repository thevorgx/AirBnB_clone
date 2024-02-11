#!/usr/bin/python3
"""unittest cases for base_model module"""



import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid

class Base_Model_Test(unittest.TestCase):


    def test_no_arg_Initialization(self):
        """test if the initializations attributes are done correctly"""

        instance = BaseModel()
        uuid_string = instance.id
        uuid_object = uuid.UUID(uuid_string)
        self.assertIsInstance(uuid_object, uuid.UUID)
        self.assertIsInstance(instance.id, str)
        self.assertIsInstance(instance.created_at, datetime)
        self.assertIsInstance(instance.updated_at, datetime)


if __name__ == "__main__":
    unittest.main()
