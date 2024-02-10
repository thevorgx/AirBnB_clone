#!/usr/bin/python3
"""command prompt class(console)"""


import cmd
import re
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""

    prompt = "(hbnb) "
    airbnb_classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
        }

    def do_quit(self, command):
        """quit when the user write the quit command"""
        return (True)

    def do_EOF(self, command):
        """quit when user use ctrl+D"""
        return (True)

    def emptyline(self):
        """execute nothing when the user hit enter without command"""
        pass

    def do_create(self, command):
        """create an instance by giving the classe name as arg"""
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
        """show an instance by giving the classe name and id as arg"""
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
        """destroy an instance by giving the classe name and id as arg"""
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
        """show all instances or instances with the same classe name"""
        classes = self.airbnb_classes
        tokenize_cmd = command.split()
        if len(tokenize_cmd) > 1:
            return
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
                cls_instances.append(str(instance))

        print(cls_instances)

    def do_update(self, command):
        """Update an instance attributes or add a new one"""
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
        instance_to_upd = f"{cls_name}.{instance_id}"
        all_instances = storage.all()
        if instance_to_upd not in all_instances:
            print("** no instance found **")
            return

        if len(tokenize_cmd) < 3:
            print("** attribute name missing **")
            return
        attri_name = tokenize_cmd[2]

        if len(tokenize_cmd) < 4:
            print("** value missing **")
            return
        else:
            instance = all_instances[instance_to_upd]
            attri_value = tokenize_cmd[3]
            if isinstance(instance.__dict__[attri_name], int):
                attri_value = int(attri_value)
            elif isinstance(instance.__dict__[attri_name], float):
                attri_value = float(attri_value)
            setattr(instance, attri_name, attri_value)
            storage.save()

    def do_count(self, command):
        """count the number of instances of a class name"""
        classes = self.airbnb_classes
        tokenize_cmd = command.split()
        if len(tokenize_cmd) != 1:
            return
        cls_name = tokenize_cmd[0]
        if cls_name not in classes:
            print("** class doesn't exist **")
            return

        count = 0
        all_instances = storage.all()
        for key in all_instances:
            if key.split('.')[0] == cls_name:
                count += 1
        print(count)

    method_class = [
        "all", "show", "destroy", "count", "update"
    ]

    def default(self, line):
        """default method when invalid command passed"""

        classes = self.airbnb_classes

        if '.' not in line and '()' not in line:
            print(f"*** Unknown syntax: {line}")
            return

        tokenize_cmd = tuple(line.split('.'))

        if not line.strip():
            return

        if tokenize_cmd[0] not in classes:
            print("** class doesn't exist **")
            return

        class_name = tokenize_cmd[0]

        if len(tokenize_cmd) < 2:
            return

        attribute_method = tokenize_cmd[1]
        if '(' in attribute_method:
            regex = r'\(["\)]+([^\)]+)\"\)'
            matches = re.findall(regex, attribute_method)
            if matches:
                regex_matches = ''.join(matches)
                if ',' and '"' in regex_matches:
                    text = regex_matches
                    regex_matches = text.replace(',', '').replace('"', '')
            attribute_method = attribute_method.split('(')[0]
            if "update" == attribute_method:
                find_third_arg = regex_matches.split()
                if find_third_arg[2]:
                    third_arg = f'"{find_third_arg[2]}"'
                    if third_arg.startswith('"') and third_arg.endswith('"'):
                        third_arg = third_arg[1:-1]
                        try:
                            third_arg = int(third_arg)
                        except ValueError:
                            try:
                                third_arg = float(third_arg)
                            except ValueError:
                                pass
                    if not isinstance(third_arg, (int, float)):
                        third_arg = f'"{third_arg}"'
                    removed_arg = find_third_arg.pop(2)
                    if isinstance(third_arg, str):
                        result_string = ''.join(third_arg)
                    else:
                        result_string = third_arg
                    find_third_arg = ' '.join(find_third_arg)
            if attribute_method not in self.method_class:
                return

        if not matches:
            expression = f"{class_name}"
        else:
            if "update" == attribute_method:
                expression = f"{class_name} {find_third_arg} {result_string}"
            else:
                expression = f"{class_name} {regex_matches}"
        if "all" == attribute_method:
            self.do_all(expression)
        elif "show" == attribute_method:
            self.do_show(expression)
        elif "destroy" == attribute_method:
            self.do_destroy(expression)
        elif "count" == attribute_method:
            self.do_count(expression)
        elif "update" == attribute_method:
            self.do_update(expression)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
