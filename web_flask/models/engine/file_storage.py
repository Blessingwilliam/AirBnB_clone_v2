#!/usr/bin/python3
"""
Contains the FileStorage class
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """serializes instances to a JSON file & deserializes back to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns the list of objects of one type of class.
        Args:
            cls (class): class type
        """
        if cls is None:
            return self.__objects
        cls_dict = {}
        for key, value in self.__objects.items():
            if type(value) == cls:
                cls_dict[key] = value
        return cls_dict

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        json_obj = {}
        for key in self.__objects:
            json_obj[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(json_obj, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                json_obj = json.load(f)
            for key in json_obj:
                class_name = key.split('.')[0]
                self.__objects[key] = eval(class_name)(**json_obj[key])
        except Exception:
            pass

    def close(self):
        """Call reload() method for deserializing the JSON file to objects"""
        self.reload()

