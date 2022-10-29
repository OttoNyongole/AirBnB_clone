#!/usr/bin/python3
"""Condole Module command interpreter"""

import cmd

class HBNBCommand(cmd.Cmd):
     """method to quit the command line interpreter
     """
     def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program"""
        print("")
        return True

    def emptyline(self):
        """Do nothing upon receiving empty line"""
        pass

    def do_create(self, arg):
        """Usage: create <class>
        Create a new class instance and print its id.
        """
        argl = shlex.split(arg)
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(argl[0])().id)
            storage.save()




if __name__=="__main__":
    HBNBCommand().cmdloop
