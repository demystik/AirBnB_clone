#!/usr/bin/python3

"""
Console Module
"""
import cmd
<<<<<<< HEAD
import sys
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
=======
>>>>>>> 61907e03ecfb1be2eac4c6fa43cbdf651811b16c


class HBNBCommand(cmd.Cmd):
    """ The AirBnB Console """
<<<<<<< HEAD
    intro = "Welcome to the HBnB console. Type help or ? to display commands\n"
=======
>>>>>>> 61907e03ecfb1be2eac4c6fa43cbdf651811b16c
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
<<<<<<< HEAD
        """Quit command to exit the program"""
        sys.exit(0)
=======
        """ Quits the console """
        return exit
>>>>>>> 61907e03ecfb1be2eac4c6fa43cbdf651811b16c

    def help_quit(self):
        print("Quit command to exit the program\n")
        return

    def help_EOF(self):
        print("End of file command to exit console")
        return

    def do_create(self, line):
        """creates an instance of BaseModel"""
        try:
            self.__com = line.split()
            if not self.__com[0]:
                print(f"** class name missing **")
            if self.__com[0] != "BaseModel":
                print(f"** class doesnt exist **")
            else:
                new_obj = BaseModel()
                new_obj.save()
                new_obj_dict = new_obj.to_dict()
                print(new_obj_dict[id])
        except IndexError:
            pass

    def do_show(self, line):
        """Prints the str rep of an instance based on the class name and id"""
        try:
            self.__com = line.split()
            print(self.__com)
            if not self.__com[0]:
                print(f"** class name missing **")
            if self.__com[0] != "BaseModel":
                print(f"** class doesn't exist **")
            if self.__com[0] and not self.__com[1]:
                print(f"** instance id missing **")
            to_show = "{}.{}".format(BaseModel.__class__.__name__,
                                     self.__com[1])
            print(self.__all_objs)
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
            if not self.__com[0]:
                print(f"** class name missing **")
            if self.__com[0] != "BaseModel":
                print(f"** class doesn't exist **")
            if not self.__com[1]:
                print(f"** instance id missing **")

            to_destroy = "{}.{}".format(BaseModel.__class__.__name__,
                                        self.__com[1])
            if to_destroy not in self.__all_objs:
                print(f"** no instance found **")
            else:
                self.__all_objs.pop(to_destory)
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
            if not self.__com[0]:
                print(f"** class name missing **")
            if self.__com[0] != "BaseModel":
                print(f"** class doesn't exist **")
            if not self.__com[1]:
                print(f"** instance id missing **")

            to_update = "{}.{}".format(BaseModel.__class__.__name__,
                                       self.__com[1])
            if to_update not in self.__all_objs:
                print(f"** no instance found **")
            if not self.__com[2]:
                print(f"** attribute name missing **")
            if not self.__com[3]:
                print(f"** value missing **")
            else:
                self.__all_objs[to_update].self.__com[2] = self.__com[3]
                self.__all_objs[to_update].save()
        except IndexError:
            pass

    def help_update(self):
        print("update {<>} {<>} {<>} \"{<>}\"".format(
              "class name", "id", "attribute name", "attribute value"))
        return


if __name__ == "__main__":
    HBNBCommand().cmdloop()
