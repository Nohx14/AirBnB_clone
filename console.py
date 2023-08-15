#!/usr/bin/env python3
"""
The console module. This module contains all
the files needed to run our console
for managing the state of our application
"""


import cmd
import shlex
import re
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    The HBNB class to control the console needed for
    our application
    """
    prompt = "(hbnb) "
    models = {'BaseModel': BaseModel, 'User': User,
              'Place': Place, 'State': State,
              'City': City, 'Amenity': Amenity,
              'Review': Review}

    def onecmd(self, line):
        """
        Base class {cmd.Cmd} method {onecmd} that has been overridden to add
        some modifications
        """
        m = re.search(r'(\w+).(\w+)\((.+)?\)', line)

        if m is not None:

            command = m.group(2)
            modelname = m.group(1)
            arguments = m.group(3)
            argL = []

            if arguments is None:
                newarg = command + ' ' + modelname

            else:
                newarg = command + ' ' + modelname

                arguments = arguments.split(', ')

                """
                This section works on the argument if the
                command to execute is update
                and if it is passed an argument of
                dictionary to work on. i.e: If you
                want to update your instance using
                a dictionary directly instead of a
                string based approach:
                Example:
                    (hbnb) User.update("ea61d516-e30f-49bf-aff7-24d66652de03",
                            {'first_name': "John", "age": 89})
                """
                if command == 'update':
                    # ----- check if a dictionary is passed -----
                    clean_exit = False
                    if arguments[1][0] == '{':

                        dict_values = self.parse_dict(arguments[1:])
                        instance_id = self.remove_quotation(arguments[0])
                        newarg = newarg + ' ' + arguments[0]

                        for dict_v in dict_values:

                            for arc in dict_v:
                                newarg = newarg + ' ' + arc

                            if cmd.Cmd.onecmd(self, newarg):
                                clean_exit = True

                            newarg = command + ' ' + modelname + \
                                ' ' + instance_id

                        if clean_exit:
                            return True
                        return
                """
                This section is for other commands if
                the command given is not an update
                command with a dictionary as argument,
                It woks with update commands also
                provided that it doesn't have a
                dictionary as it's argument,
                Example:
                    (hbnb) User.show(instance_id)
                    (hbnb) BaseModel.update("instance_id",
                    "attr_name", "attr_value")
                """
                for arg in arguments:
                    argL.append(self.remove_quotation(arg))
                # ----- add each arguments to the new argument that -----
                # ----- will be passed to onecmd -----

                for arg in argL:
                    newarg = newarg + ' ' + arg

            # ----- finally call one cmd -----
            if cmd.Cmd.onecmd(self, newarg):
                return True

        else:
            if cmd.Cmd.onecmd(self, line):
                return True

    def parse_dict(self, dictionary):
        """
        parse an argument to the update command if it is a dictionary
        """
        dict_arg = dictionary
        dict_str = ""

        for unit in dict_arg:
            dict_str += unit + ', '

        # ----- remove the last command and space in the string -----
        dict_str = dict_str[:-2]
        # ----- remove both opening and closing brackets -----
        dict_str = dict_str[1:-1]
        # ----- split each argument i.e: name: tunde, age: 24 -----
        # -----it splits it into a list of name: tunde -----
        # ----- and age: 24 -----

        dict_L = dict_str.split(', ')
        temp_dict_L = []

        for dict_unit in dict_L:

            split = dict_unit.split(':')
            temp_dict_L.append(split)

        dict_L = []
        temp_dict = []

        for dict_list in temp_dict_L:

            for dict_unit in dict_list:

                if dict_unit[0] == ' ':

                    # ----- remove spaces -----
                    dict_unit = dict_unit[1:]
                temp_dict.append(self.remove_quotation(dict_unit))

            dict_L.append(temp_dict)

            temp_dict = []
        return dict_L

    def remove_quotation(self, string):
        """
        remove quotes from arguments
        """
        # ----- remove the double quotes they have -----
        if string[0] == '\'' or string[0] == '\"':
            string = string[1:-1]
        return string

    def do_quit(self, line):
        """
        command to exit the console
        Usage:
            (hbnb) quit
        """
        return True

    def do_EOF(self, line):
        """
        close the console when EOF is encountered
        EOF: End-Of-File
        """
        return True

    def emptyline(self):
        """
        do nothing when nothing is entered as a comand
        """
        pass

    def do_create(self, line):
        """
        creates a new instance of a class given
        as an argument
        Usage:
            (hbnb) create <class name>
        """
        if not line:
            print("** class name missing **")

        elif line not in HBNBCommand.models.keys():
            print("** class doesn't exist **")

        else:

            # ----- create a new instance of the class -----
            # ----- stated and save to a file -----
            new_model = HBNBCommand.models[line]()
            new_model.save()
            print(new_model.id)

    def do_show(self, line):
        """
        Prints the string representation of an instance
        based on the class name and id given to the command as
        argument
        Usage:
            (hbnb) show <class name> <instance id>
        """
        line = tuple(line.split())

        try:

            classname = line[0]
            if classname not in HBNBCommand.models.keys():
                print("** class doesn't exist **")
                return

        except IndexError:

            print("** class name missing **")
            return

        try:
            instance_id = line[1]

        except IndexError:
            print("** instance id missing **")
            return

        full_search_t = f"{classname}.{instance_id}"
        storage.reload()
        inst_object = storage.all()

        try:
            print(inst_object[full_search_t])

        except KeyError:
            print("** no instance found **")

    def do_destroy(self, line):
        """
        deletes an instance based on the class name and id
        and saved the change into the JSON file
        Usage:
            (hbnb) destroy <class name> <instance id>
        """
        line = tuple(line.split())
        try:

            classname = line[0]
            if classname not in HBNBCommand.models.keys():

                print("** class doesn't exist **")
                return

        except IndexError:

            print("** class name missing **")
            return

        try:
            instance_id = line[1]

        except IndexError:

            print("** instance id missing **")
            return

        full_search_t = f"{classname}.{instance_id}"
        storage.reload()
        inst_object = storage.all()
        try:

            del inst_object[full_search_t]
            storage.save()

        except KeyError:
            print("** no instance found **")

    def do_all(self, line):
        """
            Prints all the string representation of all instances
            Can be based on the class name if the class name is given,
            Otherwise just print all
            Usage:
                (hbnb) all
                    It will list all instances
                (hbnb) all <class name>
                    It will list instances belonging to the specified
                    class name
        """
        if line and line not in HBNBCommand.models.keys():

            print("** class doesn't exist **")
            return

        storage.reload()
        inst_object = storage.all()
        to_print = []
        if line:

            # ----- if the class name exist print it's instances -----
            for value in inst_object.values():

                if value.__class__.__name__ == line:
                    to_print.append(str(value))

        else:

            for value in inst_object.values():
                to_print.append(str(value))

        if to_print:
            print(to_print)

    def do_count(self, line):
        """
        counts the amount of instance a given class has
        """
        if line and line not in HBNBCommand.models.keys():

            print("** class doesn't exist **")
            return

        storage.reload()
        inst_object = storage.all()
        instances = []
        if line:

            for value in inst_object.values():

                if value.__class__.__name__ == line:
                    instances.append(str(value))

        else:

            for value in inst_object.values():
                instances.append(str(value))
        print(len(instances))

    def do_update(self, line):
        """
        Updates an instance based on the class name given
        and the attribute-value pair given as argument
        Usage:
            update <class name> <id> <attribute name> \"<attribute value>\"
        """
        errors = {0: "** class name missing **",
                  1: "** instance id missing **",
                  2: "** attribute name missing **",
                  3: "** value missing **"}

        arg_idx = ["class_name", "instance_id", "attr_name",
                   "attr_value"]

        arguments = {"class_name": "", "instance_id": "",
                     "attr_name": "", "attr_value": ""}

        line = shlex.split(line)

        # ----- check if all neccesary arguments are given -----
        for i in range(4):

            try:

                arguments[arg_idx[i]] = line[i]
                # ----- checks if the class name given is valid -----
                if i == 0:

                    if arguments[arg_idx[0]] not in HBNBCommand.models.keys():
                        print("** class doesn't exist **")
                        return

                # ----- checks if the inst id given is valid -----
                if i == 1:

                    class_name = arguments[arg_idx[0]]
                    instance_id = arguments[arg_idx[1]]
                    if not self.check_instance_id(class_name, instance_id):
                        return

            except IndexError:
                print(errors[i])
                return
        full_search_t = f"{class_name}.{instance_id}"
        storage.reload()
        inst_object = storage.all()
        to_update = inst_object[full_search_t]
        attr_name = arguments["attr_name"]
        attr_value = arguments["attr_value"]
        # ----- set the attribute and save it to the storage engine -----

        try:
            attr_value = type(getattr(to_update, attr_name))(attr_value)

        except AttributeError:
            attr_value = str(attr_value)

        setattr(to_update, arguments["attr_name"], attr_value)
        storage.save()

    def check_instance_id(self, class_name, instance_id):
        """
        checks if the instance id given as argument is valid
        """
        full_search_t = f"{class_name}.{instance_id}"
        storage.reload()
        inst_object = storage.all()
        # ----- check if the id arg given is valid -----
        try:

            inst_object[full_search_t]
            return True

        except KeyError:

            print("** no instance found **")
            return False


def check_instance_id(class_name, instance_id):
    """
    checks if the instance id given as argument is valid.
    I left this same function as the method in the HBNBCommand
    class because this was where it was before I moved it as a
    method, I might have associated some code with this function
    and I don't want to break my code so I left this here.
    As time comes I will keep checking my codebase to see
    where else I am using this function in order to change it's
    use to the method in the HBNBCommand class
    """
    full_search_t = f"{class_name}.{instance_id}"
    storage.reload()
    inst_object = storage.all()
    # ----- check if the id arg given is valid -----
    try:

        inst_object[full_search_t]
        return True

    except KeyError:

        print("** no instance found **")
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
