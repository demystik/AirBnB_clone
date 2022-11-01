#!/usr/bin/python3
"""
Defines the Review Module
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """The Usser Class"""
    place_id = ""
    user_id = ""
    text = ""


if __name__ == "__main__":
    Review()
