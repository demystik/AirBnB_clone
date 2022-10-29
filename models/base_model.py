#!/usr/bin/python3
import uuid
from datetime import datetime
import models
"""
The Base Class module
"""


class BaseModel:
    """BaseModel class"""
    def __init__(self, *args, **kwargs):
        """initializes an instance of BaseModel"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key == "__class__":
                    continue
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """prints in the form: [<class name>] (<self.id>) <self.__dict__>"""
        rep = "[{}] ({}) {}"
        return rep.format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of the instance """
        new_dict = self.__dict__.copy()
        new_dict.update({'__class__': str(self.__class__.__name__)})
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict


if __name__ == "__main__":
    BaseModel()
