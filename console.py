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

    def do_show(self, line=""):
        """Show command to print the string representation of an instance
        """
        if line == "":
            print("** class name missing **")
        else:
            args = self.my_split(line)
            if args[0] not in storage.cls_mapping().keys():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                obj = storage.all()
                cls_id = f"{args[0]}.{args[1]}"

                if cls_id in obj.keys():
                    print(obj[cls_id])
                else:
                    print("** no instance found **")

    def do_all(self, line=""):
        """All command to print the string representation of all instances
            based or not on the class name
        """
        inst_list = []
        if line == "":
            obj = storage.all()
            inst_list = [f"{inst}" for inst in obj.values()]
        else:
            args = self.my_split(line)

            if args[0] not in storage.cls_mapping().keys():
                print("** class doesn't exist **")
            else:
                obj = storage.all().values()
                for inst in obj:
                    if inst.__class__.__name__ == args[0]:
                        inst_list.append(str(inst))
        print(inst_list)

    def do_destroy(self, line=""):
        """destroy command deletes an instance based on the class name and id
        """
        if line == "":
            print("** class name missing **")

        else:
            args = self.my_split(line)
            if args[0] not in storage.cls_mapping().keys():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                obj = storage.all()
                cls_id = f"{args[0]}.{args[1]}"

                if cls_id in obj.keys():
                    del obj[cls_id]
                    storage.save()
                else:
                    print("** no instance found **")

    def do_update(self, line=""):
        """update command updates an instance based on the class name and id
            by adding or updating attribute
        """
        if line == "":
            print("** class name missing **")
        else:
            args = self.my_split(line)
            arg_len = len(args)
            obj = storage.all()

            if args[0] not in storage.cls_mapping().keys():
                print("** class doesn't exist **")
            elif arg_len < 2:
                print("** instance id missing **")
            elif f"{args[0]}.{args[1]}" not in obj.keys():
                print("** no instance found **")
            elif arg_len < 3:
                print("** attribute name missing **")
            elif arg_len < 4:
                print("** value missing **")
            else:
                cls_id = f"{args[0]}.{args[1]}"
                if hasattr(obj[cls_id], args[2]):
                    # Get the attribute and verify it's type
                    attr_type = type(getattr(obj[cls_id], args[2]))
                    if attr_type is int:
                        args[3] = int(args[3])
                    elif attr_type is float:
                        args[3] = float(args[3])
                setattr(obj[cls_id], args[2], args[3])
                obj[cls_id].save()

    def my_split(self, line):
        """Custom function for extracting arguments"""
        import shlex
        return shlex.split(line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
