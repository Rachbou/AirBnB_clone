#!/usr/bin/python3

"""Defines the HBNB command line."""


import cmd


class HBNBCommand(cmd.Cmd):
    """Hbnb command processor."""

    prompt = '(hbnb) '

    def emptyline(self):
        """Empty line method"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""

        print()
        return True

    def help_quit(self):
        """Help command for quit"""
        print("Quit command to exit the program\n")

    def do_EOF(self, line):
        """EOF command to exit the program"""
        print()
        return True

    def help_EOF(self):
        """Help command for EOF"""
        print("EOF command to exit the program\n")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
