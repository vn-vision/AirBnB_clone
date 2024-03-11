#!/usr/bin/python3
''' the first user '''
from models.base_model import BaseModel


class User(BaseModel):
    ''' This class user inherits from BaseModel '''

    email = ""
    password = ""
    first_name = ""
    last_name = ""
