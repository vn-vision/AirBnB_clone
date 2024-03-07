#!/usr/bin/python3
''' convert dictionary representation to a json string
json is standaerd representation of a data structure '''
import json
from importlib import import_module
from json.decoder import JSONDecodeError

class FileStorage():
    ''' IT SERILIZES INSTANCES TO A JSON FILE '''

    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        ''' sets in __objects the obj with key <obj class name>.id '''
        if obj:
            key ="{}.{}".format(type(obj).__name__, obj.id)
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
            des_dict = {}
            with open(self.__file_path, 'r') as f:
                des_dict = json.loads(f.read())

            self.__objects = {key:eval(obj["__class__"])(**obj)
                    for key, obj in des_dict.items()}
        except (FileNotFoundError, JSONDecodeError):
            pass

    def all(self):
        ''' returns the __objects dictionary '''
        return self.__objects
