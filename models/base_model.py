#!/usr/bin/python3
''' The BaseModel class, introduction to Airbnb'''
import uuid
from datetime import datetime


class BaseModel():
    ''' The class model with different functions '''

    def __init__(self, *args, **kwargs):
        ''' the initialization function, initialzing
        different attributes '''

        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        value = datetime.strptime(
                                value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)
        else:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        ''' updates new records and records the time '''
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        ''' returns a dictionary with class, name, model,
        time it was created and updated '''

        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = type(self).__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()

        return obj_dict

    def __str__(self):
        ''' return the statement of the BaseModel '''
        from models import storage
        return ("[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__))
