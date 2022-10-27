#!/usr/bin/pythob3
"""Condole Module command interpreter"""

import cmd

class HBNBCommand(cmd.Cmd):

     """method to quit the command line interpreter"""
    def do_quit(self, arg):
        """quit the command prompt"""
        return True

