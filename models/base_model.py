#!/usr/bin/python3
""" BaseModel class Defination."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """the BaseModel Representaion"""

    def __init__(self, *args, **kwargs):
        """new BaseModel Initialization.

        Args:
             *args won’t be :used
            **kwargs : Key&&value pairs of attributes.
        """
        first = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for y, z in kwargs.items():
                if y == "created_at" or y == "updated_at":
                    self.__dict__[y] = datetime.strptime(z, first)
                else:
                    self.__dict__[y] = z
        else:
            models.storage.new(self)

    def save(self):
        """last var update."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """represent self as a dictionary"""
        store = self.__dict__.copy()
        store["created_at"] = self.created_at.isoformat()
        store["updated_at"] = self.updated_at.isoformat()
        store["__class__"] = self.__class__.__name__
        return store

    def __str__(self):
        """Return representation of the BaseModel instance."""
        classname = self.__class__.__name__
        return "[{}] ({}) {}".format(classname, self.id, self.__dict__)
