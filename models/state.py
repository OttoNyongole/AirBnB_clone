#!/usr/bin/python3
"""Defines State class."""
from models.base_model import BaseModel


class State(BaseModel):
    """Inherits rom BaseModel represents State.
    Public attribute:
                    name(str): name of the state
    """
    name = ""
