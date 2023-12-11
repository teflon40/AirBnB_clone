#!/usr/bin/python3
"""This module defines a class that saves and retrieves data
    to and from JSON files
"""
import json


class FileStorage:
    """File storage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        """Adds a new obj to a dictionary
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Saves data to json file as a dictionary of
            <class name>.id : obj.__dict__
        """
        new_dict = {}
        with open(FileStorage.__file_path, "w", encoding='utf-8') as jsonfile:
            for key, obj in FileStorage.__objects.items():
                new_dict[key] = obj.to_dict()
            json.dump(new_dict, jsonfile)

    def reload(self):
        """Load saved data from json file as a dictionary of
            <class name>.id : obj
        """
        from models.base_model import BaseModel
        try:
            with open(FileStorage.__file_path, "r", encoding='utf-8') as file:
                jsondata = json.load(file)
                for values in jsondata.values():
                    cls_name = values['__class__']
                    cls_name = self.cls_mapping()[cls_name]
                    self.new(cls_name(**values))
        except FileNotFoundError:
            pass

    def cls_mapping(self):
        """Returns a mapping of various classes as a dictionary"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        return {
                "BaseModel": BaseModel,
                "User": User,
                "State": State,
                "City": City,
                "Amenity": Amenity,
                "Place": Place,
                "Review": Review
                }
