#!/usr/bin/python3
''' Command line interpreter for the airbnb '''
import cmd
from models.base_model import BaseModel as BM
from models.engine.file_storage import FileStorage as FS


class HBNBCommand(cmd.Cmd):
    ''' this is the class definition '''
    prompt = '(hbnb) '

    def validation(self, args):
        ''' this is a custom function to check class name '''

        cl_miss = "** class name missing **"
        cl_NA = "** class doesn't exist **"

        if not args:
            print(cl_miss)
            return False

        if args[0] != "BaseModel" and args[0] != "all":
            print(cl_NA)
            return False
        return True

    def check_instance(self, args, details):
        ''' check if instace exists '''
        if len(args) < 2:
            print("** instance id missing **")
            return None

        if args[1] not in details:
            print("** no instance found **")
            return None

        return details[args[1]]

    def do_quit(self, line):
        ''' Quit command to exit the program '''
        return True

    def do_EOF(self, line):
        ''' Exit the program on  EOF  signal (Ctrl + D) '''
        print()
        return True

    def emptyline(self):
        ''' Do nothing on empty input line '''
        pass

    def do_create(self, line):
        ''' Creates a new instance of BaseModel,
        saves it to JSON file and prints the id
        `usage create BaseModel`
        '''

        args = line.split()
        if not self.validation(args):
            return

        instance = BM()
        FS().save()
        print(instance.id)

    def do_show(self, line):
        ''' Prints the string representation
        of an instance based on class Name '''

        args = line.split()
        if not self.validation(args):
            return

        details = FS().reload()
        instance = self.check_instance(args, details)
        if instance:
            print(instance)

    def do_destroy(self, line):
        ''' Deletes an instance given class name and id '''

        args = line.split()
        if not self.validation(args):
            return

        details = FS().reload()
        if details:
            instance = self.check_instance(args, details)
            if instance:
                del details[args[1]]
                FS().save()

    def do_all(self, line):
        ''' Show representation of all instances based
        or not in on the class name '''

        args = line.split()
        if not self.validation(args):
            return

        details = FS().reload()
        if details:
            if args and args[0] == 'all':
                for instance in details.values():
                    print(instance)
            elif args:
                instances = [instance for instance in details.values()
                             if instance.__class__.__name__ == args[0]]
                if instances:
                    for instance in instances:
                        print(instance)
                else:
                    print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
