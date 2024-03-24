#!/usr/bin/python3

"""
    Defines a class Amenity.
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represent a Amenity."""

    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize a new Amenity"""

        super().__init__(*args, **kwargs)
