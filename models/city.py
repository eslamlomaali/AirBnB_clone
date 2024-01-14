#!/usr/bin/python3
"""City class Defination"""
from models.base_model import BaseModel


class City(BaseModel):
    """city representaion.

    Attributes:
        state_id (str): state id.
        name (str): city name.
    """

    state_id = ""
    name = ""
