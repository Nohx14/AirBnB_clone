#!/usr/bin/python3
"""
Module that contains the class city,
It handles all the logic associated with city
data for our application
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    A City class to handle our city data inn our application
    Attributes:
        state_id: Id of the stateit belongs to.
        name: name of the city
    """
    state_id = ""
    name = ""
