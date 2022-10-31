#!/usr/bin/python3

"""
Console Module
"""
import cmd
import sys
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """ The AirBnB Console """
    prompt = "(hbnb) "
    file = None
    __com = ""
    __all_objs = models.storage.all()

    # ------ basic console commands -------
    def emptyline(self):
        """Used to handle emptyline which by default
        would have execute previous command"""
        pass

    def do_EOF(self, line):
        """End of file command to exit console"""
        return True

    def do_quit(self, line):
        """ Quits the console """
        return exit

    def help_quit(self):
        print("Quit command to exit the program\n")
        return

    def help_EOF(self):
        print("End of file command to exit console")
        return

    def help_create(self):
        print("creates a new instance of BaseModel and prints the id")
        return

    def help_destroy(self):
        print("deletes an instance based on the class name and id")
        return

    def help_show(self):
        print("Prints the string representation of an instance
              based on the class name and id")
        return

    def help_all(self):
        print("Prints the string representation of all instances")
        return

    def do_create(self, line):
        """creates an instance of BaseModel"""
        try:
            self.__com = line.split()
            if len(self.__com) < 1:
                print(f"** class name missing **")
            elif self.__com[0] != "BaseModel":
                print(f"** class doesnt exist **")
            else:
                new_obj = BaseModel()
                new_obj.save()
                new_obj_dict = new_obj.to_dict()
                print(new_obj_dict["id"])
        except exception as e:
            pass

    def do_show(self, line):
        """Prints the str rep of an instance based on the class name and id"""
        try:
            self.__com = line.split()
            if len(self.__com) < 1:
                print(f"** class name missing **")
            elif self.__com[0] != "BaseModel":
                print(f"** class doesn't exist **")
            elif len(self.__com) < 2:
                print(f"** instance id missing **")
            else:
                to_show = "{}.{}".format("BaseModel", self.__com[1])
                if to_show not in self.__all_objs:
                    print(f"** no instance found **")
                else:
                    print(self.__all_objs[to_show].__str__())
        except IndexError:
            pass

    def do_destroy(self, line):
        """deletes an instance based on the class name and id"""
        try:
            self.__com = line.split()
            if len(self.__com) < 1:
                print(f"** class name missing **")
            elif self.__com[0] != "BaseModel":
                print(f"** class doesn't exist **")
            elif len(self.__com) < 2:
                print(f"** instance id missing **")
            else:
                to_destroy = "{}.{}".format("BaseModel", self.__com[1])
                if to_destroy not in self.__all_objs:
                    print(f"** no instance found **")
                else:
                    self.__all_objs.pop(to_destroy)
                    models.storage.save()
        except IndexError:
            pass

    def do_all(self, line):
        """prints all string representation of instances"""
        try:
            self.__com = line.split()
            if self.__com[0] != "BaseModel":
                print(f"** class doesn't exist **")
            else:
                models.storage.reload()
                rep = []
                for key, value in self.__all_objs.items():
                    rep.append(value.__str__())
                print(rep)
        except IndexError:
            pass

    def do_update(self, line):
        """Updates an instance based on the class name and id"""
        try:
            self.__com = line.split()
            if len(self.__com) < 1:
                print(f"** class name missing **")
            elif self.__com[0] != "BaseModel":
                print(f"** class doesn't exist **")
            elif len(self.__com) < 2:
                print(f"** instance id missing **")
            elif len(self.__com) < 3:
                print(f"** attribute name missing **")
            elif len(self.__com) < 4:
                print(f"** value missing **")
            else:
                to_update = "{}.{}".format("BaseModel", self.__com[1])
                if to_update not in self.__all_objs:
                    print(f"** no instance found **")
                else:
                    obj = self.__all_objs[to_update]
                    attr = ""
                    for i in self.__com[3]:
                        if i != '\"':
                            attr = attr + i

                    setattr(obj, (self.__com[2]), attr)
                    self.__all_objs[to_update].save()
        except IndexError:
            pass

    def help_update(self):
        print("update <{}> <{}> <{}> \"<{}>\"".format(
              "class name", "id", "attribute name", "attribute value"))
        return


if __name__ == "__main__":
    HBNBCommand().cmdloop()
