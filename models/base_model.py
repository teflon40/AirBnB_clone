#!/usr/bin/python3
"""This module defines a class BaseModel which is the base model
    of the AirBnB Clone webapp
"""
from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """Base Model"""
    def __init__(self, *args, **kwargs):
        """Initialize public instance attributes with **kwargs
        """
        if kwargs:
            del kwargs['__class__']
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """Overrides default __str__ and returns the
            string representation of an object
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the public instance attribute updated_at with the current
            datetime and saves to a JSON file
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns the dictionary representation of and object
        """
        new_dict = {'__class__': self.__class__.__name__}
        for key, value in self.__dict__.items():
            if key == 'created_at' or key == 'updated_at':
                value = value.isoformat()
            new_dict[key] = value
        return dict(new_dict)
