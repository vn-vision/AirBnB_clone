#!/usr/bin/python3
''' This script defines a class BaseModel
It defines all common attributes/methods for other classes
'''
import uuid
import datetime


class BaseModel():
    id = str(uuid.uuid4())

    print(type(id), id)
