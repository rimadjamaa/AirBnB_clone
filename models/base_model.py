#!/usr/bin/python3
"""
This module defines the BaseModel class which is the base class for all models.
"""

import uuid
from datetime import datetime
import json


class BaseModel:
    """A base class for all AirBnB models."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance."""
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
            # if 'created_at' in kwargs and isinstance(self.created_at, str):
            #     self.created_at = datetime.
            # strptime(kwargs['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
            # if 'updated_at' in kwargs and isinstance(self.updated_at, str):
            #     self.updated_at = datetime.
            # strptime(kwargs['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def save(self):
        """Updates the public instance attribute
        updated_at with the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all
        keys/values of __dict__ of the instance."""
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict

    def __str__(self):
        """Returns a string representation of the instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
