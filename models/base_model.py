''' The BaeModel class, introduction to Airbnb'''
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
                        value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def save(self):
        ''' updates new records and records the time '''
        self.updated_at = datetime.now()

    def to_dict(self):
        ''' returns a dictionary with class, name, model,
        time it was created and updated '''

        obj_dict = {'my_number': self.my_number,
                    'name': self.name,
                    '__class__': type(self).__name__,
                    'updated_at': self.updated_at.isoformat(),
                    'id': self.id,
                    'created_at': self.created_at.isoformat(),}
        return obj_dict

    def __str__(self):
        return ("[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__))
