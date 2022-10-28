#!/usr/bin/python3
"""Review class that inherits from BaseModel"""

class review(BaseModel):
    """
    Public attributes:
                    place_id(str): it will be the place.id
                    user_id(str): it will be the user.id
                    text(str): the review comment
    """
    place_id = ""
    user_id = ""
    text = ""
