#!/usr/bin/python3
''' Command line interpreter for the airbnb '''
import cmd

class HBNBCommand(cmd.Cmd):
    ''' this is the class definition '''
    prompt = '(hbnb) '
    
    def do_quit(self, line):
        ''' command exits the program '''
        return True

    def do_EOF(self, line):
        ''' exit the program on  quit signal '''
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
