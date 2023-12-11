#!/usr/bin/python3
"""This module defines a class User which models a real life user
"""

from models.base_model import BaseModel


class User(BaseModel):
    """Simulating a real life user"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

#    def __init__(self):
#        """Instantiate object"""
#        super().__init__()
