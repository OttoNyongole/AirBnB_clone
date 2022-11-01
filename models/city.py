#!/usr/bin/python3
"""Defines City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Inherits BaseModel represents a city.
    class for cities
    Public Attributes:
                    state_id(str): The state id
                    name(str): The name of the city
    """
    state_id = ""
    name = ""
