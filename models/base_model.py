#!/usr/bin/python3
"""the base model"""


import uuid
from datetime import datetime
import models


class BaseModel:
    """BaseModel class"""

    def __init__(self, *args, **kwargs):
        """special method that initialize the public instance attributes"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        setattr(
                            self,
                            key,
                            datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                    else:
                        setattr(self, key, value)
        models.storage.new(self)

    def __str__(self):
        """special method that return a formated string ready to be printed"""
        f_string = f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
        return (f_string)

    def save(self):
        """Update 'updated_at' attribute and save changes to storage"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """method that return a dict containing different attributes"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return (new_dict)
