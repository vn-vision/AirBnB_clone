#!/usr/bin/python3
''' FileStorage class '''
import json


class FileStorage:
    ''' this class saves data in json file and reloads
    when needed'''

    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        ''' sets in __objects in the obj
        with key <obj class name>.id'''

        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        ''' serializes __objects to JSON file '''

        try:
            with open(self.__file_path, 'r') as f:
                prev_data = json.load(f)
        except FileNotFoundError:
            prev_data = {}

        ser_dict = {key: value.to_dict()
                    for key, value in self.__objects.items()}

        prev_data.update(ser_dict)
        with open(self.__file_path, 'w') as f:
            json.dump(prev_data, f)

    def reload(self):
        ''' deserializes JSON file to __objects
        if the file exists'''
        try:
            from models.base_model import BaseModel
            with open(self.__file_path, 'r') as f:
                des_dict = json.load(f)
            for key, value in des_dict.items():
                class_name, obj_id = key.split('.')
                cls = self.get_class(class_name)
                if cls:
                    self.__objects[key] = cls(**value)
                else:
                    print("Class not found:", class_name)

        except (FileNotFoundError, json.JSONDecodeError):
            pass

    def all(self):
        ''' returns the dictionary __objects '''
        return self.__objects

    def get_class(self, class_name):
        if class_name == "BaseModel":
            from models.base_model import BaseModel
            return BaseModel
        else:
            return None  # Return None if class is not found
