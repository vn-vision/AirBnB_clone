#!/usr/bin/python3
''' Command line interpreter for the airbnb '''
import cmd


class HBNBCommand(cmd.Cmd):
    ''' this is the class definition '''
    prompt = '(hbnb) '

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
