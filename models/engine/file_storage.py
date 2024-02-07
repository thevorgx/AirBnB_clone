#!/usr/bin/python3
"""file storage model"""


from models.base_model import BaseModel
from os.path import isfile
import json
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """FileStorage class"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return the dict __objects of stored instances in FileStorage"""
        return (self.__objects)

    def new(self, obj):
        """add a new obj to the __objects dictionary"""
        object_key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[object_key] = obj

    def save(self):
        """Serialize data (objs to dicts) and save to JSON file"""
        dict_objects = {}
        path = FileStorage.__file_path
        for key, value in self.__objects.items():
            dict_objects[key] = value.to_dict()
        with open(path, "w", encoding="UTF-8") as f:
            json.dump(dict_objects, f, indent = 4)

    def reload(self):
        """deserialize data from JSON file to objs and load into __objects"""
        path = self.__file_path
        if isfile(path):
            with open(path, "r") as f:
                dict_objects = json.load(f)
            for key, value in dict_objects.items():
                cls_name, obj_id = key.split(".")
                cls_instance = eval(cls_name)(**value)
                self.__objects[key] = cls_instance
