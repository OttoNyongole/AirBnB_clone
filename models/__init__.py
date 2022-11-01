#!/usr/bin/python3
"""
__init__ magic method for modes directry
"""

from models.engine.file_storage import FileStorage
from .base_model import BaseModel

storage = FileStorage()
storage.reload()
