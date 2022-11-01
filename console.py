#!/usr/bin/python3

"""Definies the HBnB Console Module"""
import cmd
import sys
import re
from shlex import split
import models
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parse(arg):
    curly_braces = re.search(r"\{(.?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [e.strip(",") for e in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            ret1 = [e.strip(",") for e in lexer]
            ret1.append(brackets.group())
            return ret1
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        ret1 = [e.strip(",") for e in lexer]
        ret1.append(curly_braces.group())
        return ret1


class HBNBCommand(cmd.Cmd):
    """ Defines the HolbertonBnB command interpreter.
    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "
    file = None
    __classes = {
            "BaseModel",
            "User",
            "State",
            "City",
            "Place",
            "Amenity",
            "Review"
    }

    # ------ basic console commands -------
    def emptyline(self):
        """Used to handle emptyline which by default
        would have executed previous command"""
        pass

    def default(self, arg):
        """Default behaviour for cmd module when input is invalid"""
        argdict = {
                "all": self.do_all,
                "show": self.do_show,
                "destroy": self.do_destroy,
                "count": self.do_count,
                "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            arg1 = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", arg1[1])
            if match is not None:
                command = [arg1[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(arg1[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_EOF(self, line):
        """End of file signal to exit console"""
        return True

    def do_quit(self, line):
        """ Quits command to exit the console """
        return exit

    def do_create(self, line):
        """Usage: create <class> <key 1>=<value 2> <key 2>=<value 2> ...
        Create a new class instance with given keys/values and print its id.
        """
        try:
            if not line:
                raise SyntaxError()
            my_com = line.split()

            kwargs = {}
            for i in range(1, len(my_com)):
                key, value = tuple(my_com[i].split("="))
                if value[0] == '"':
                    value = value.strip('"').replace("_", " ")
                else:
                    try:
                        value = eval(value)
                    except (SyntaxError, NameError):
                        continue
                kwargs[key] = value
            if kwargs == {}:
                obj = eval(my_com[0])()
            else:
                obj = eval(my_com[0])(**kwargs)
                storage.new(obj)
            print(obj.id)
            obj.save()

        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Usage: show <class> <id> or <class>.show(<id>)
        Displays the string representation of a class instance of a given id.
        """
        arg1 = parse(line)
        objdict = storage.all()
        if len(arg1) == 0:
            print(f"** class name missing **")
        elif arg1[0] not in HBNBCommand.__classes:
            print(f"** class doesn't exist **")
        elif len(arg1) == 1:
            print(f"** instance id missing **")
        elif "{}.{}".format(arg1[0], arg1[1]) not in objdict:
            print(f"** no instance found **")
        else:
            print(objdict["{}.{}".format(arg1[0], arg1[1])])

    def do_destroy(self, line):
        """Usage: destroy <class> <id> or <class>.destroy(<id>)
        Deletes a class instance of a given id."""
        arg1 = parse(line)
        objdict = storage.all()
        if len(arg1) == 0:
            print(f"** class name missing **")
        elif arg1[0] not in HBNBCommand.__classes:
            print(f"** class doesn't exist **")
        elif len(arg1) == 1:
            print(f"** instance id missing **")
        elif "{}.{}".format(arg1[0], arg1[1]) not in objdict.keys():
            print(f"** no instance found **")
        else:
            del objdict["{}.{}".format(arg1[0], arg1[1])]
            storage.save()

    def do_all(self, line):
        """Usage: all or all <class> or <class>.all()
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects."""
        arg1 = parse(line)
        if len(arg1) > 0 and arg1[0] not in HBNBCommand.__classes:
            print(f"** class doesn't exist **")
        else:
            obj_rep = []
            for obj in storage.all().values():
                if len(arg1) > 0 and arg1[0] == obj.__class__.__name__:
                    obj_rep.append(obj.__str__())
                elif len(arg1) == 0:
                    obj_rep.append(obj.__str__())
            print(obj_rep)

    def do_count(self, line):
        """Usage: count <class> or <class>.count()
        Retrieve the number of instances of a given class. """
        arg1 = parse(arg)
        count = 0
        for obj in storage.all().values():
            if arg1[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, line):
        """Usage: update <class> <id> <attribute_name> <attribute_value> or
        <class>.update(<id>, <attribute_name>, <attribute_value>) or
        <class>.update(<id>, <dictionary>)
        Updates a class instance of a given id by adding or updating a
        given attribute key/value pair or dictionary."""
        arg1 = parse(line)
        objdict = storage.all()
        if len(arg1) == 0:
            print(f"** class name missing **")
            return False
        if arg1[0] not in HBNBCommand.__classes:
            print(f"** class doesn't exist **")
            return False
        if len(arg1) == 1:
            print(f"** instance id missing **")
            return False
        if "{}.{}".format(arg1[0], arg1[1]) not in objdict.keys():
            print(f"** no instance found **")
            return False
        if len(arg1) == 2:
            print(f"** attribute name missing **")
            return False
        if len(arg1) == 3:
            try:
                type(eval(arg1[2])) != dict
            except NameError:
                print(f"** value missing **")
                return False

        if len(arg1) == 4:
            obj = objdict["{}.{}".format(arg1[0], arg1[1])]
            if arg1[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.dict__[arg1[2]])
                obj.__dict__[arg1[2]] = valtype(arg1[3])
            else:
                obj.__dict__[arg1[2]] = arg1[3]
        elif type(eval(arg1[2])) == dict:
            obj = objdict["{}.{}".format(arg1[0], arg1[1])]
            for k, v in eval(arg1[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
