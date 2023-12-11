#!/usr/bin/python3
"""This module defines a class HBNBCommand which makes use of
    the cmd module to interpret commands
"""
from models.base_model import BaseModel
import cmd
from models import storage


class HBNBCommand(cmd.Cmd):
    """Console class"""
    prompt = '(hbhb) '

    def emptyline(self):
        """Overrides Cmd.emptyline()"""
        pass

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """Ctrl-D to exit program
        """
        print()
        return True
