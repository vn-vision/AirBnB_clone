#!/usr/bin/python3
''' This script defines a class BaseModel
It defines all common attributes/methods for other classes
'''
import uuid
import datetime


class BaseModel():
    ''' This is a BaseModel class, it has a unique ID,
    it has timestamp for when it was created and updates
    '''

    def __init__(self):
        ''' Initialize BaseModel with unique id and timestamps '''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        ''' this is the output format of the basemodel'''

        return ("[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__))

    
    def save(self):
        ''' updates the public instance attribute updated_at'''
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        ''' returns a dictionary containing all keys/values of __dict__
        a key __class__ must be added to this dictionary
        '''
        dict_rep = self.__dict__.copy()
        dict_rep['__class__'] = type(self).__name__
        dict_rep['created_at'] = self.created_at.isoformat()
        dict_rep['updated_at'] = self.updated_at.isoformat()

        return dict_rep
