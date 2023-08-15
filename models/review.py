#!/usr/bin/python3
"""
A module to handle the manipulation of
data for review given by the customer or app user
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review:
        handles and manipulates the data given by the user
        for reviews
    """
    place_id = ""
    user_id = ""
    text = ""
