#!/usr/bin/python3
''' this is the review module '''
from models.base_model import BaseModel


class Review(BaseModel):
    ''' Review class '''
    place_id = ""
    user_id = ""
    text = ""
