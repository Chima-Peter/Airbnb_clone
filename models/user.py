#!/usr/bin/env python3
"""
The module that contains the USER class
"""
from models.base_model import BaseModel
from datetime import datetime
from uuid import uuid4
import models


class User(BaseModel):
    """
    The class User that inherits the BaseModel class
    """
    email = ""
    first_name = ""
    last_name = ""
    password = ""

    def __init__(self, *args, **kwargs):
        """
        Initialises the class with values and sets it for storage
        """
        super().__init__(*args, **kwargs)