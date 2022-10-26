#!/usr/bin/python3

"""
Console Module
"""
import cmd
import sys


class Console(cmd.Cmd):
    """ The AirBnB Console """
    intro = "Welcome to the HBnB console. Type help or ? to display commands\n"
    prompt = "(hbnb)"
    file = None

    # ------ basic console commands -------
    def do_EOF(self, line):
        """End of file"""
        return True

    def do_quit(self, line):
        """ Quits the console """
        sys.exit(0)


if __name__ == "__main__":
    Console().cmdloop()
