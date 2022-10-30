#!/usr/bin/python3

"""
Console Module
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """ The AirBnB Console """
    prompt = "(hbnb) "
    file = None

    # ------ basic console commands -------
    def emptyline(self):
        """Used to handle emptyline which by default
        would have execute previous command"""
        pass

    def do_EOF(self, line):
        """End of file"""
        return True

    def do_quit(self, line):
        """ Quits the console """
        return exit


if __name__ == "__main__":
    HBNBCommand().cmdloop()
