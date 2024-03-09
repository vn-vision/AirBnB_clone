#!/usr/bin/python3
''' This script defines a class BaseModel
It defines all common attributes/methods for other classes
'''
import uuid
import datetime
from models import storage


class BaseModel():
    ''' This is a BaseModel class, it has a unique ID,
    it has timestamp for when it was created and updates
    '''

    def __init__(self, *args, **kwargs):
        ''' Initialize BaseModel with unique id and timestamps '''

        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updatd_at']:
                        value = datetime.datetime.strptime(
                                value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)

    def save(self):
        ''' updates the public instance attribute updated_at'''
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        ''' returns a dictionary containing all keys/values of __dict__
        a key __class__ must be added to this dictionary'''

        dict_rep = self.__dict__.copy()
        dict_rep["__class__"] = type(self).__name__
        dict_rep['created_at'] = self.created_at.strftime(
                '%Y-%m-%dT%H:%M:%S.%f')

        ''' Check if updated_at is a string, if so,  storage.save()
        convert it to a datetime object'''
        if isinstance(self.updated_at, str):
            dict_rep['updated_at'] = datetime.datetime.strptime(
                    self.updated_at, '%Y-%m-%dT%H:%M:%S.%f')
        else:
            dict_rep['updated_at'] = self.updated_at.strftime(
                    '%Y-%m-%dT%H:%M:%S.%f')

        return dict_rep

    def __str__(self):
        ''' updates the public instance attribute updated_at '''

        return ("[{}] ({}) {}".format(type(self).__name__,
                                      self.id, self.__dict__))
