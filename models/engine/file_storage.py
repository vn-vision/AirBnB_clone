import json
from importlib import import_module
from json.decoder import JSONDecodeError


class FileStorage:
    ''' IT SERIALIZES INSTANCES TO A JSON FILE '''

    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        ''' sets in __objects the obj with key <obj class name>.id '''
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        ''' serializes __objects to the json file path __FILE_PATH '''
        if self.__objects:
            ser_dict = {}
            for key, value in self.__objects.items():
                ser_dict[key] = value.to_dict()
            with open(self.__file_path, 'w', encoding='utf-8') as f:
                json.dump(ser_dict, f)

    def reload(self):
        ''' deserializes the json file to __objects '''
        try:
            with open(self.__file_path, 'r') as f:
                des_dict = json.load(f)

                self.__objects = {k: self.load_instance(k, v)
                                  for k, v in des_dict.items()}

        except FileNotFoundError:
            print("File not found, creating a new one...")
        except JSONDecodeError:
            print("Error decoding JSON file, creating a new one...")

    def load_instance(self, key, value):
        ''' Dynamically loads the instance based on class name '''
        from models.base_model import BaseModel
        class_name, obj_id = key.split('.')
        cls = BaseModel
        return cls(**value)

    def all(self):
        ''' returns the __objects dictionary '''
        return self.__objects
