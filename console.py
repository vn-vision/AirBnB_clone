#!/usr/bin/python3
''' Console for HBNB '''
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.city import City
from models.state import State
from models.review import Review
from models.place import Place
from models.amenity import Amenity


class HBNBCommand(cmd.Cmd):
    '''HBNB Command Interpreter'''

    prompt = '(hbnb) '

    def emptyline(self):
        '''Empty line + ENTER shouldn’t execute anything'''
        pass

    def do_quit(self, arg):
        '''Quit command to exit the program'''
        return True

    def do_EOF(self, line):
        '''Quit command to exit the program'''
        return True

    def do_create(self, arg):
        '''Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id'''

        if not arg:
            print("** class name missing **")
            return

        arg = arg.split()
        if arg[0] not in ['BaseModel', 'User', 'State',
                          'City', 'Amenity', 'Place', 'Review']:
            print("** class doesn't exist **")

        try:
            new_instance = eval(arg[0])()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        '''Prints the string representation of an instance
        based on the class name and id'''

        if not arg:
            print("** class name missing **")
            return

        arg = arg.split()

        if arg[0] not in ['BaseModel', 'User', 'State',
                          'City', 'Amenity', 'Place', 'Review']:
            print("** class doesn't exist **")
            return

        if len(arg) == 1:
            print("** instance id missing **")
            return

        key = "{}.{}".format(arg[0], arg[1])
        objects = storage.all()

        if key not in objects:
            print("** no instance found **")
            return

        print(objects[key])

    def do_destroy(self, arg):
        '''Deletes an instance based on the class name and id'''

        if not arg:
            print("** class name missing **")
            return

        arg = arg.split()

        if arg[0] not in ['BaseModel', 'User', 'State',
                          'City', 'Amenity', 'Place', 'Review']:
            print("** class doesn't exist **")
            return

        if len(arg) == 1:
            print("** instance id missing **")
            return

        key = "{}.{}".format(arg[0], arg[1])
        objects = storage.all()

        if key not in objects:
            print("** no instance found **")
            return

        del objects[key]
        storage.save()

    def do_all(self, arg):
        '''Prints all string representation of
        all instances based or not on the class name'''

        objects = storage.all()
        if not arg:
            print([str(obj) for obj in objects.values()])
            return

        arg = arg.split()

        if arg[0] not in ['BaseModel', 'User', 'State',
                          'City', 'Amenity', 'Place', 'Review']:
            print("** class doesn't exist **")
            return

        print([str(obj) for key, obj in objects.items() if arg[0] in key])

    def do_update(self, arg):
        '''Updates an instance based on the class name and id'''

        if not arg:
            print("** class name missing **")
            return

        arg = arg.split()

        if arg[0] not in ['BaseModel', 'User', 'State',
                          'City', 'Amenity', 'Place', 'Review']:
            print("** class doesn't exist **")
            return

        if len(arg) == 1:
            print("** instance id missing **")
            return

        key = "{}.{}".format(arg[0], arg[1])
        objects = storage.all()

        if key not in objects:
            print("** no instance found **")
            return

        if len(arg) == 2:
            print("** attribute name missing **")
            return

        if len(arg) == 3:
            print("** value missing **")
            return

        setattr(objects[key], arg[2], arg[3])
        objects[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
