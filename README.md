# 0x00. AirBnB clone - The console

**The AirBnB Project entails the following**
  **.** A Parent class (**BaseModel**) to take care of the initialization, serialization, and deserialization of
        future instances
  **.** Create a simple flow of serialization/deserialization: **instance <-> Dictionary <-> JSON string <-> file**
  **.** Create all classes used for AirBnB (**User, State, City, Place...**) that inherit from **BaseModel**
  **.** Create the first abstracted storage engine of the project: **File storage.**
  **.** Create all unittests to validate all classes and storage engine.

**The Command Interpreter**
The command interpreter is almost like a shell, but it is limited to a specific use-case. It's mainly used to manage
the objects of our project.

It can be used to perform various tasks such as:
  **.** create a new object(ex: a new User or a new Place)
  **.** retrieve an object from a file, a databse etc...
  **.** do operation on objects(count, compute stats, etc...)
  **.** update attributes of an object
  **.** destory an object

**How to Start the Console**
To startup the console, simply type in your commandline.

**Your shell should work like this in interactive mode:**

$ ./console.py

Welcome to the AirBnB console. Type help or ? to display commands
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
(hbnb)
(hbnb) quit
$

**But also in non-interactive mode:**
$ echo "help" | ./console.py(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
