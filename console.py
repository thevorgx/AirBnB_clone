#!/usr/bin/python3
"""command prompt class(console)"""


import cmd


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""

    prompt = "(hbnb) "

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
