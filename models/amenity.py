#!/usr/bin/python3
"""
A module that handles all the logic and data that has to do with
the amenities for our app that each location has.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class that handles the amenities each location
    in our application has.
    attributes:
        name: the name of the amenity
    """
    name = ""
