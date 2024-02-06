#!/usr/bin/python3
"""command prompt class(console)"""


import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""

    prompt = "(hbnb) "
    airbnb_classes = {"BaseModel": BaseModel}

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

    def do_show(self, command):
        classes = self.airbnb_classes
        tokenize_cmd = command.split()

        if not tokenize_cmd:
            print("** class name missing **")
            return

        cls_name = tokenize_cmd[0]

        if cls_name not in classes:
            print("** class doesn't exist **")
            return

        try:
            instance_id = tokenize_cmd[1]
        except IndexError:
            print("** instance id missing **")
            return

        instance_to_find = f"{cls_name}.{instance_id}"
        all_instances = storage.all()
        if instance_to_find not in all_instances:
            print("** no instance found **")
            return

        instance_to_show = all_instances[instance_to_find]
        print(instance_to_show)

    def do_destroy(self, command):
        classes = self.airbnb_classes
        tokenize_cmd = command.split()

        if not tokenize_cmd:
            print("** class name missing **")
            return

        cls_name = tokenize_cmd[0]

        if cls_name not in classes:
            print("** class doesn't exist **")
            return

        if len(tokenize_cmd) < 2:
            print("** instance id missing **")
            return

        instance_id = tokenize_cmd[1]
        instance_to_del = f"{cls_name}.{instance_id}"
        all_instances = storage.all()
        if instance_to_del not in all_instances:
            print("** no instance found **")
            return

        del all_instances[instance_to_del]
        storage.save()


    def do_all(self, command):
        classes = self.airbnb_classes
        tokenize_cmd = command.split()
        if not tokenize_cmd:
            all_instances = storage.all().values()
            all_instances_list = []
            for instance in all_instances:
                all_instances_list.append(str(instance))
            print(all_instances_list)
            return

        cls_name = tokenize_cmd[0]

        if cls_name not in classes:
            print("** class doesn't exist **")
            return

        cls_instances = []
        instances = storage.all().values()

        for instance in instances:
            if type(instance).__name__ == cls_name:
                print(type(instance).__name__)
                cls_instances.append(str(instance))

        print(cls_instances)

        
if __name__ == '__main__':
    HBNBCommand().cmdloop()
