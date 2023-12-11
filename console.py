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
        return shlex.split(line)

    def do_create(self, line=""):
        """Create command to create a new instance
        """
        if line:
            args = self.my_split(line)
            if args[0] in storage.cls_mapping().keys():
                cls_name = storage.cls_mapping()[args[0]]
                obj = cls_name()
                obj.save()
                print(obj.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop("Welcome to AirBnB Console")
