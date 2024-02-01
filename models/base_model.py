#!/usr/bin/python3
"""the base model"""


import uuid
from datetime import datetime


class BaseModel:
    """BaseModel class"""

    def __init__(self):
        """special method that initialize the public instance attributes"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """special method that return a formated string ready to be printed"""
        f_string = f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
        return (f_string)

    def save(self):
        """method that Update the 'updated_at' attr to the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """method that return a dict containing different attributes"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return (new_dict)
