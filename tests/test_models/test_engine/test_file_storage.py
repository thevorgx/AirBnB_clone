#!/usr/bin/python3
"""unittest cases for file_storage module"""


import unittest
from models.engine.file_storage import FileStorage

class File_Storage_Test(unittest.TestCase):
    """Base_Model_Test class (unittests for the base_model)"""
    def test_all_method(self):
        """test the all method"""

        storage = FileStorage()
        all_objects = storage.all()

        self.assertIsInstance(all_objects, dict)
        self.assertEqual(all_objects, storage._FileStorage__objects)


if __name__ == "__main__":
    unittest.main()
