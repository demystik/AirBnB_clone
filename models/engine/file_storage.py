#!/usr/bin/python3
"""
The FileStorage Module to serialize and deserialize instances of
objects to a JSON file
"""
from models.base_model import BaseModel
import json


class FileStorage:
    """serializes and deserializes instances to a JSON file"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary of BaseModel instances"""
        return self.__objects

    def new(self, obj):
        """updates __objects with key-value pair of new instances"""
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
                dict_obj = json.load(fp)
                print(dict_obj)
            for key, value in dict_obj.items():
                self.__objects[key] = eval(key.split(".")[0])(**value)
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    FileStorage()
