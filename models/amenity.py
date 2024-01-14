#!/usr/bin/python3

""" Amenity class defination."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """amenity Represention.

    Attributes:
        name (str): amenity's name.
    """

    name = ""
