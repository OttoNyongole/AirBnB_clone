#!/usr/bin/python3
"""
__init__ magic method for modes directry
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()