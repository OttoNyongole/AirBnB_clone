#!/usr/bin/python3
"""Defines Review class."""


from models.base_model import BaseModel


class Review(BaseModel):
    """Inherits rom BaseModel represents a review."""
    place_id = ""
    user_id = ""
    text = ""