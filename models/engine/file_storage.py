import json


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        ser_dict = {key: value.to_dict() for key, value in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(ser_dict, f)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as f:
                des_dict = json.load(f)
                self.__objects = {k: self.load_instance(k, v) for k, v in des_dict.items()}
        except FileNotFoundError:
            # Properly handle file not found error
            print("File not found:", self.__file_path)
        except json.JSONDecodeError:
            # Properly handle JSON decoding error
            print("Error decoding JSON file:", self.__file_path)

    def load_instance(self, key, value):
        from models.base_model import BaseModel

        class_name, obj_id = key.split('.')
        if class_name not in globals():
            print("Class not found:", class_name)
            return None

        cls = globals()[class_name]
        return cls(**value)

    def all(self):
        return self.__objects
