#!/usr/bin/python3
"""
Defines the City Module
"""

from models.base_model import BaseModel


class City(BaseModel):
    """The City Class"""
    state_id = ""
    name = ""


if __name__ == "__main__":
    City()
