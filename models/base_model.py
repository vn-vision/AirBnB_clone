#!/usr/bin/python3
''' This script defines a class BaseModel
It defines all common attributes/methods for other classes
'''
import uuid
from datetime import datetime
# from models import storage


class BaseModel():
    ''' This is a BaseModel class, it has a unique ID,
    it has timestamp for when it was created and updates
    '''

    def __init__(self, *args, **kwargs):
        ''' Initialize BaseModel with unique id and timestamps '''

        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        value = datetime.strptime(
                                value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            now = datetime.now()
            self.created_at = now
            self.updated_at = now
            # storage.new(self)

    def save(self):
        ''' updates the public instance attribute updated_at'''
        self.updated_at  = datetime.now()

    def to_dict(self):
        ''' returns a dictionary containing all keys/values of __dict__
        a key __class__ must be added to this dictionary'''

        if hasattr(self, 'my_number'):
            my_num = self.my_number
        if hasattr(self, 'name'):
            name = self.name

        dict_rep = {'my_number': my_num,
                    'name': name,
                    '__class__': type(self).__name__,
                    'updated_at': self.updated_at.isoformat(),
                    'id': self.id,
                    'created_at': self.created_at.isoformat()
                    }

        return dict_rep


    def __str__(self):
        ''' updates the public instance attribute updated_at '''

        return ("[{}] ({}) {}".format(type(self).__name__,
                                      self.id, self.__dict__))
