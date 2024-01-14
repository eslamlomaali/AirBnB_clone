#!/usr/bin/python3
"""FileStorage class defination."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """storage engine repesentaion as abstract.

    Attributes:
        __file_path (str): file name to save the obj
        __objects (dict): instantiated objects as a dict.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """dictionary of __objects is return."""
        return FileStorage.__objects

    def new(self, o):
        """Set in __objects"""
        ret = o.__class__.__name__
        FileStorage.__objects["{}.{}".format(ret, o.id)] = o

    def save(self):
        """Sequnce of __objects to the JSON file"""
        o2 = FileStorage.__objects
        o3 = {o: o2[o].to_dict() for o in o2.keys()}
        with open(FileStorage.__file_path, "w") as fille:
            json.dump(o3, fille)

    def reload(self):
        """No sequence of the  __file_path to __objects."""
        try:
            with open(FileStorage.__file_path) as fille2:
                o3 = json.load(fille2)
                for obj in o3.values():
                    class_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(class_name)(**obj))
        except FileNotFoundError:
            return
