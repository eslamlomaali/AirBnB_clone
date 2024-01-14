#!/usr/bin/python3

"""__init__ method for directory (global)"""
from models.engine.file_storage import FileStorage

"""return instance of storage"""
storage = FileStorage()
storage.reload()
