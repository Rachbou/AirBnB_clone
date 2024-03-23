#!/usr/bin/python3

"""
    Defines a class BaseModel.
"""

from datetime import datetime
from uuid import uuid4


class BaseModel:
    """Represent a BaseModel."""

    def __init__(self):
        """Initialize a new BaseModel"""

        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Return a string representation of the class"""

        return "[{:s}] ({:s}) {:s}".format(
            self.__class__.__name__,
            self.id,
            str(self.__dict__)
        )

    def save(self):
        """Update the date field"""

        self.updated_at = datetime.now()

    def to_dict(self):
        """Return a dictionary representation of the instance"""

        rep = {
            "__class__": self.__class__.__name__,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }

        dict_copy = self.__dict__.copy()
        dict_copy.update(rep)
        return (dict_copy)
