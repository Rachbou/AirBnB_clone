#!/usr/bin/python3

"""
    Defines a class City.
"""

from models.base_model import BaseModel


class City(BaseModel):
    """Represent a City."""

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize a new City"""

        super().__init__(*args, **kwargs)
