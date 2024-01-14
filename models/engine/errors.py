#!/usr/bin/python3
"""errors in file storage defination """


class ModelNotFoundError(Exception):
    """unknown module is passed"""
    def __init__(self, arg="BaseModel"):
        super().__init__(f"Model his name is {arg} is not found!")


class InstanceNotFoundError(Exception):
    """unknown id  is passed"""

    def __init__(self, obj_id="", mod="BaseModel"):
        super().__init__(
                f"Insatnce not exist!")
