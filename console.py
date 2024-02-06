#!/usr/bin/python3
"""command prompt class(console)"""


import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""

    prompt = "(hbnb) "
    airbnb_classes = ["BaseModel"]

    def do_quit(self, command):
        """quit when the user write the quit command"""
        return (True)

    def do_EOF(self, command):
        """quit when user use ctrl+D"""
        return (True)

    def help_quit(self):
        """print documentation for the "quit" command"""
        print("Quit command to exit the program")

    def emptyline(self):
        """execute nothing when the user hit enter without command"""
        pass

    def do_create(self, command):
        classes = self.airbnb_classes
        tokenize_cmd = command.split()

        if not tokenize_cmd:
            print("** class name missing **")
            return

        cls_name = tokenize_cmd[0]

        if cls_name not in classes:
            print("** class doesn't exist **")
            return
        creation_expression = f"{cls_name}()"
        create_instance = eval(creation_expression)
        storage.save()
        print(create_instance.id)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
