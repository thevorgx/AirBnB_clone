#!/usr/bin/python3
"""unittest cases for file_storage module"""


import unittest
import json
import os
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

    def test_deserialize_data_method(self):
        """test reload(deserialize) method"""

        storage = FileStorage()
        obj = BaseModel()
        storage.new(obj)
        storage.save()
        storage.reload()

        object_key = f"{obj.__class__.__name__}.{obj.id}"

        self.assertIn(object_key, storage.all())
    
    def test_file_storage_initialization(self):
        """test the initialization of file storage script"""

        storage = FileStorage()
        storage.reload()
        all_objects = storage.all()

        self.assertIsInstance(all_objects, dict)
        self.assertTrue(all_objects)

    def test_create_json(self):
        """test if the json file created correctly"""

        file_path = "file.json"
        if os.path.isfile(file_path):
            os.remove(file_path)

        storage = FileStorage()
        storage.save()

        self.assertTrue(os.path.isfile(file_path))

if __name__ == "__main__":
    unittest.main()
