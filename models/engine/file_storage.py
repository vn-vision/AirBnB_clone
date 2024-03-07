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

            for key, obj in des_dict.items():
                class_name = obj["__class__"]
                module_name = "models.base_model"
                module = import_module(module_name)
                cls = getattr(module, class_name)
                self.__objects[key] = cls(**obj)

        except (FileNotFoundError, JSONDecodeError):
            pass

    def all(self):
        ''' returns the __objects dictionary '''
        return self.__objects

