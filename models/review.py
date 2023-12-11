#!/usr/bin/python3
"""This module defines a class State which models real life state
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Simulates reviews"""
    place_id = ""
    user_id = ""
    text = ""
