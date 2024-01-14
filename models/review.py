#!/usr/bin/python3
""" Review class defination."""
from models.base_model import BaseModel


class Review(BaseModel):
    """review  representaion.

    Attributes:
        place_id (str): Place id.
        user_id (str): User id.
        text (str): review text.
    """

    place_id = ""
    user_id = ""
    text = ""
