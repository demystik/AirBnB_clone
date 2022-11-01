#!/usr/bin/python3
"""
The FileStorage Module to serialize and deserialize instances of
objects to a JSON file
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """serializes and deserializes instances to a JSON file"""
    __file_path = "file.json"
    __objects = {}
    class_dict = {"BaseModel": BaseModel, "User": User, "Place": Place,
                  "Amenity": Amenity, "City": City, "Review": Review,
                  "State": State}

    def all(self):
        """returns the dictionary of BaseModel instances"""
        return self.__objects

    def new(self, obj):
        """updates __objects with key-value pair of new instances"""
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """ serializes __objects to JSON file """
        obj_dict = {}

        for key, value in self.__objects.items():
            obj_dict[key] = value.to_dict()
        with open(self.__file_path, mode="w", encoding="utf-8") as fp:
            json.dump(obj_dict, fp)

    def reload(self):
        """ deserializes the JSON file to __objects """
        try:
            with open(self.__file_path, mode="r", encoding="utf-8") as fp:
                new_obj_dict = json.load(fp)
            for key, value in new_obj_dict.items():
                obj = self.class_dict[value["__class__"]](**value)
                self.__objects[key] = obj
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    FileStorage()
