#!/usr/bin/pythob3
"""Condole Module command interpreter"""

import cmd

class HBNBCommand(cmd.Cmd):

     """method to quit the command line interpreter"""
    def do_quit(self, arg):
        """quit the command prompt"""
        return True

    def do_EOF(self, arg):
        """
        EOF signal to quit the console.
        """
        print("")
        return True

if __name__=="__main__":
    HBNBCommand().cmdloop
