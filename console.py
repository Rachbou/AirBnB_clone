#!/usr/bin/python3

"""Defines the HBNB command line."""


import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage
import json


class HBNBCommand(cmd.Cmd):
    """Hbnb command processor."""

    prompt = '(hbnb) '
    __classes = ["BaseModel", "User", "State",
                 "City", "Amenity", "Place", "Review"]
    __commands = ["all", "count", "show", "destroy", "update"]

    def precmd(self, line):
        """ Get the line before interpretate"""
        if len(line):
            line_command = line.split()
            if len(line_command):
                update_dict = line.split("{")
                update_command = line.split("\"")
                line_command = line_command[0].split("(")
                class_command = line_command[0].split(".")
                if len(line_command) == 2:
                    args = line_command[1].split("\"")
                else:
                    return line
                if len(class_command) == 2\
                    and class_command[0] in self.__classes\
                    and class_command[1] in self.__commands:
                    command = ' '.join(class_command[-1::-1])
                    if line_command[1] == ")":
                        return command
                    elif len(args) == 3 and args[2] == ")":
                        return ' '.join([command, args[1]])
                    elif len(update_command) == 5\
                        and update_command[4] != ")"\
                        and update_command[4][-1] == ")":
                        value = update_command[4].strip(')').split()[1]
                        final = ' '.join([command, args[1],
                                          update_command[3],
                                          value])
                        return final
                    elif len(update_command) == 7\
                        and update_command[6] == ")":
                        final = ' '.join([command, args[1],
                                          update_command[3],
                                          update_command[5]])
                        return final
                    elif len(update_dict):
                        try:
                            dict_up = json.loads(
                                str("{" + update_dict[1][:-1].replace("'",
                                                                      "\"")))
                            command = ' '.join([class_command[0], args[1]])
                            for key, value in dict_up.items():
                                final = command + " \"" + key + "\"" +\
                                    " \"" + str(value) + "\""
                                self.do_update(final)
                            command = ' '.join([class_command[1], final])
                            return command
                        except:
                            return line
                    else:
                        return line
                else:
                    return line
            else:
                return line
        else:
            return line

    def emptyline(self):
        """Empty line method"""

        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""

        return True

    def help_quit(self):
        """Help command for quit"""

        print("Quit command to exit the program\n")

    def do_EOF(self, line):
        """EOF command to exit the program"""

        return True

    def help_EOF(self):
        """Help command for EOF"""

        print("EOF command to exit the program\n")

    def do_create(self, arg):
        """Create a BaseModel and save the json in a file"""

        if len(arg) > 0:
            list_arg = arg.split()
            if list_arg[0] in HBNBCommand.__classes:
                print(eval(list_arg[0])().id)
                storage.save()
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def help_create(self):
        """Help command for create"""

        print("Creates a new BaseModel, saves it and prints the id\n")

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id"""

        if len(arg) > 0:
            list_arg = arg.split()
            objects = storage.all()
            if len(list_arg) >= 2:
                clsId = ''.join([list_arg[0], '.', list_arg[1]])
                if list_arg[0] not in self.__classes:
                    print("** class doesn't exist **")
                elif clsId in objects:
                    print(objects[clsId])
                else:
                    print("** no instance found **")
            elif len(list_arg) == 1:
                objs_cls = [e.split('.')[0] for e in list(objects.keys())]
                if arg not in objs_cls:
                    print("** class doesn't exist **")
                else:
                    print("** instance id missing **")
        else:
            print("** class name missing **")

    def help_show(self):
        """Help command for show"""

        msg = ' '.join(["Prints the string representation",
                        "of an instance based on the",
                        "class name and id\n"])
        print(msg)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""

        if len(arg) > 0:
            list_arg = arg.split()
            objects = storage.all()
            if len(list_arg) >= 2:
                clsId = ''.join([list_arg[0], '.', list_arg[1]])
                if list_arg[0] not in self.__classes:
                    print("** class doesn't exist **")
                elif clsId in objects:
                    del objects[clsId]
                    storage.save()
                else:
                    print("** no instance found **")
            elif len(list_arg) == 1:
                objs_cls = [e.split('.')[0] for e in list(objects.keys())]
                if arg not in objs_cls:
                    print("** class doesn't exist **")
                else:
                    print("** instance id missing **")
        else:
            print("** class name missing **")

    def help_destroy(self):
        """Help command for destroy"""

        print("Deletes an instance based on the class name and id\n")

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name"""

        objects = storage.all()
        if len(arg) > 0:
            list_arg = arg.split()
            clsObjs = [str(value) for key, value in objects.items()
                       if list_arg[0] == key.split('.')[0]]
            if len(clsObjs) > 0:
                print(clsObjs)
            else:
                print("** class doesn't exist **")
        else:
            allObjs = [str(v) for k, v in objects.items()]
            print(allObjs)

    def help_all(self):
        """Help command for all"""

        msg = ' '.join(["Prints all string representation of",
                        "all instances based or not on the class name\n"])
        print(msg)

    def do_count(self, arg):
        """Count how much instances have a given class"""
        if len(arg) > 0:
            list_arg = arg.split()
            all_instances = storage.all()
            if list_arg[0] in self.__classes:
                num = 0
                for key, value in all_instances.items():
                    if list_arg[0] in key:
                        num = num + 1
                print(num)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def help_count(self):
        """Help command for count"""

        msg = "Count how much instances have a given class\n"
        print(msg)

    def do_update(self, arg):
        """Updates an instance based on the class name
        and id by adding or updating attribute"""

        if len(arg) > 0:
            objects = storage.all()
            list_arg = arg.split()
            if len(list_arg) == 1:
                clsObjs = [str(v) for k, v in objects.items()
                           if arg == k.split('.')[0]]
                if len(clsObjs) > 0:
                    print("** instance id missing **")
                else:
                    print("** class doesn't exist **")
            elif len(list_arg) == 2:
                clsId = '.'.join(list_arg)
                if list_arg[0] not in self.__classes:
                    print("** class doesn't exist **")
                elif clsId in objects:
                    print("** attribute name missing **")
                else:
                    print("** no instance found **")
            elif len(list_arg) == 3:
                clsId = ''.join([list_arg[0], '.', list_arg[1]])
                if list_arg[0] not in self.__classes:
                    print("** class doesn't exist **")
                elif clsId in objects:
                    if list_arg[2]:
                        print("** value missing **")
                else:
                    print("** no instance found **")
            else:
                clsId = ''.join([list_arg[0], '.', list_arg[1]])
                if list_arg[0] not in self.__classes:
                    print("** class doesn't exist **")
                elif clsId in objects:
                    if list_arg[2]:
                        obj = objects[clsId]
                        setattr(obj, list_arg[2], list_arg[3])
                        obj.save()
                    else:
                        print("** value missing **")
                else:
                    print("** no instance found **")
        else:
            print("** class name missing **")

    def help_update(self):
        """Help command for update"""

        msg = ' '.join(["Updates an instance based on",
                        "the class name and id",
                        "by adding or updating attribute",
                        "\nUsage: update <class name> <id> <attribute name>",
                        "\"<attribute value>\"\n"])
        print(msg)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
