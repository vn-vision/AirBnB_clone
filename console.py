#!/usr/bin/python3
''' always start with shebang '''
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import shlex
import json


class HBNBCommand(cmd.Cmd):
    ''' Command line interpreter for the Airbnb '''

    prompt = '(hbnb) '

    def do_create(self, arg):
        ''' Creates a new instance of BaseModel '''
        if not arg:
            print("** class name missing **")
            return

        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        ''' Prints the string representation of an instance '''
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return

        try:
            class_name = args[0]
            if len(args) < 2:
                print("** instance id missing **")
                return

            objects = FileStorage().reload()
            key = "{}.{}".format(class_name, args[1])
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        ''' Deletes an instance based on the class name and id '''
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return

        try:
            class_name = args[0]
            if len(args) < 2:
                print("** instance id missing **")
                return

            objects = FileStorage().reload()
            key = "{}.{}".format(class_name, args[1])
            if key in objects:
                del objects[key]
                FileStorage().save()
            else:
                print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

    def do_all(self, arg):
        ''' Prints all instances '''
        args = shlex.split(arg)
        objects = FileStorage().reload()

        if not arg:
            print([str(obj) for obj in objects.values()])
            return

        try:
            class_name = args[0]
            print(
                    [str(obj) for key, obj in objects.items()
                     if key.split('.')[0] == class_name])
        except NameError:
            print("** class doesn't exist **")

    def do_update(self, arg):
        ''' Updates an instance '''
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return

        try:
            class_name = args[0]
            if len(args) < 2:
                print("** instance id missing **")
                return

            objects = FileStorage().reload()
            key = "{}.{}".format(class_name, args[1])
            if key not in objects:
                print("** no instance found **")
                return

            if len(args) < 3:
                print("** attribute name missing **")
                return

            if len(args) < 4:
                print("** value missing **")
                return

            obj = objects[key]
            setattr(obj, args[2], args[3].strip('"'))
            obj.save()
        except NameError:
            print("** class doesn't exist **")

    def do_EOF(self, arg):
        ''' Exit the program on EOF signal (Ctrl + D) '''
        return True

    def do_quit(self, arg):
        ''' Quit command to exit the program '''
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
