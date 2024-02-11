#!/usr/bin/python3
"""unittest cases for file_storage module"""


import unittest
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class File_Storage_Test(unittest.TestCase):
    """Base_Model_Test class (unittests for the base_model)"""

    def test_all_method(self):
        """test for the all method"""

        storage = FileStorage()
        all_objects = storage.all()

        self.assertIsInstance(all_objects, dict)
        self.assertEqual(all_objects, storage._FileStorage__objects)

    def test_new_method(self):
        """test for the new method"""

        storage = FileStorage()
        obj = BaseModel()

        object_key = f"{obj.__class__.__name__}.{obj.id}"
        storage.new(obj)

        self.assertIn(object_key, storage.all())
    def test_serialize_data_method(self):
        """test save(serialize) method"""
        storage = FileStorage()
        obj = BaseModel()
        storage.new(obj)
        storage.save()

        with open("file.json", "r") as f:
            data = json.load(f)
        object_key = f"{obj.__class__.__name__}.{obj.id}"

        self.assertIn(object_key, data)


if __name__ == "__main__":
    unittest.main()
