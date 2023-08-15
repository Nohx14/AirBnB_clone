#!/usr/bin/python3
"""
Module for a user class that inherits from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class:
        Defines attributes for the user
        Can be used to manage User state and data
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
