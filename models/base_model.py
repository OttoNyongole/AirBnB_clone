#!/usr/bin/python3
"""Base model class"""

import uuid
import datetime
import models

class BaseModel():
    """Class that defines all common attributes/methods for other classes"""
    def __init__(self, *arg, **kwargs):
        """
        Args:
                *rags any list args used
                **kwargs (dict) key value pair of attribute
        """
        if kwargs:
            for k, v in kwargs.items():
                if k != "__class__":
                    setattr(self, k, v)
            if hasattr(self, "created_at") and \
                    type(self.created_at) is str:
                        self.updated_at = datetime.strptime(kwargs["created_at"], tform)
            if hasattr(self, "updated_at") and \
                    type(self.updated_at) is str:
                        self.updated_at = datetime.strptime(kwargs["updated_at"], tform)
            else:
                self.id = str(uuid())
                self.created_at = datetime.now()
                self.updated_at = self.created_at
                models.storage.new(self)
                models-storage.save()
    def __str__(self):
        """Return the print presentation of the base model"""
        clname = self.__class__.__name__
        return "[{}]({}) {}".format(clname, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with the current datetime"""
        self.update_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all key/value pair of __dict__"""
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

