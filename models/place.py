#!/usr/bin/python3
"""Module class that inherits from BaseModel"""

from models.base_module import BaseModel

class Place(BaseModel):
    """
    Public class attributes:
    city_id(str): it will e the city.id
    user_id(str): it will be the user.id
    name(str): name of the place
    description(str): Discription of the place
    number_rooms(int): room number of the place
    number_bathrooms(int): number of bathrooms in the place
    mx_guest(int): how many guest can the place accomodate 
    price_by_night(int): price per room per night
    latitude(float): elevation from sea level
    logitude(float): Location of the place
    amenity_ids(str): list of Amenity.id
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
