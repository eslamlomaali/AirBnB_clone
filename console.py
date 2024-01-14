#!/usr/bin/python3
"""console defination."""
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

def p(arg):
    c = re.search(r"\{(.*?)\}", arg)
    b = re.search(r"\[(.*?)\]", arg)
    if c is None:
        if b is None:
            return [i.strip(",") for i in split(arg)]
        else:
            l = split(arg[:b.span()[0]])
            r = [z.strip(",") for z in l]
            r.append(b.group())
            return r
    else:
        l = split(arg[:c.span()[0]])
        r = [z.strip(",") for z in l]
        r.append(c.group())
        return r


class HBNBCommand(cmd.Cmd):
    """Defines interpreter.

    Attributes:
        prompt (str)    """

    p = "(hbnb) "
    __cllaa = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def empty_l(self):
        """Do nothing to do"""
        pass

    def funct(self, arg):
        """ cmd Default behavior """
        ar = {
            "all": self.all_6, # 6_all
            "show": self.show_4, # 4_show
            "destroy": self.destroy_5, # 5_destroy
            "count": self.count_7, # 7_count
            "update": self.update_8 # 8_update
        }
        m = re.search(r"\.", arg)
        if m is not None:
            a = [arg[:m.span()[0]], arg[m.span()[1]:]]
            m = re.search(r"\((.*?)\)", a[1])
            if m is not None:
                comm = [arg[1][:m.span()[0]], m.group()[1:-1]]
                if comm[0] in ar.keys():
                    helpp = "{} {}".format(a[0], comm[1])
                    return ar[comm[0]](helpp)
        print("*** syntax is Unknown: {}".format(arg))
        return False

    def quit_1(self, arg): #  1_quit
        """Quit command"""
        return True

    def EOF_2(self, arg): # 2_EOF
        """EOF signal"""
        print("")
        return True

    def create_3(self, arg): # 3_create
        """create class
        Create a new class instance.
        """
        a = p(arg)
        if len(a) == 0:
            print("** class name  is missing **")
        elif a[0] not in HBNBCommand.__cllaa:
            print("** class doesn't exist **")
        else:
            print(eval(a[0])().id)
            storage.save()

    def show_4(self, arg): 
        """show class id || class.show(id)
        class representation.
        """
        a = p(arg)
        ob = storage.all()
        if len(a) == 0:
            print("** class name is missing **")
        elif a[0] not in HBNBCommand.__cllaa:
            print("** class doesn't exist **")
        elif len(a) == 1:
            print("** instance id is missing **")
        elif "{}.{}".format(a[0], a[1]) not in ob:
            print("** no instance is found **")
        else:
            print(ob["{}.{}".format(a[0], a[1])])

    def destroy_5(self, arg):
        """destroy class id || class.destroy(id)
        Delete a class instance"""
        a = p(arg)
        ob = storage.all()
        if len(a) == 0:
            print("** class name is missing **")
        elif a[0] not in HBNBCommand.__cllaa:
            print("** class doesn't exist **")
        elif len(a) == 1:
            print("** instance id is missing **")
        elif "{}.{}".format(a[0], a[1]) not in ob.keys():
            print("** no instance found **")
        else:
            del ob["{}.{}".format(a[0], a[1])]
            storage.save()

    def all_6(self, arg):
        """all || all class || class.all()
        Display string representations of all instances."""
        a = p(arg)
        if len(a) > 0 and a[0] not in HBNBCommand.__cllaa:
            print("** class doesn't exist **")
        else:
            ol = []
            for o in storage.all().values():
                if len(a) > 0 and a[0] == o.__class__.__name__:
                    ol.append(o.__str__())
                elif len(a) == 0:
                    ol.append(o.__str__())
            print(ol)

    def count_7(self, arg):
        """count class || class.count()
        return the number of instances"""
        a = p(arg)
        co = 0
        for o in storage.all().values():
            if a[0] == o.__class__.__name__:
                co += 1
        print(co)

    def update_8(self, arg):
        """update class id attribute_name attribute_value ||
       class.update(id, attribute_name, attribute_value) ||
       class.update(id, dictionary)
        Update a class instance"""
        a = p(arg)
        ob = storage.all()

        if len(a) == 0:
            print("** class name is missing **")
            return False
        if a[0] not in HBNBCommand.__cllaa:
            print("** class doesn't exist **")
            return False
        if len(a) == 1:
            print("** instance id is missing **")
            return False
        if "{}.{}".format(a[0], a[1]) not in ob.keys():
            print("** no instance is found **")
            return False
        if len(a) == 2:
            print("** attribute name is missing **")
            return False
        if len(a) == 3:
            try:
                type(eval(a[2])) != dict
            except NameError:
                print("** value is missing **")
                return False

        if len(a) == 4:
            o = ob["{}.{}".format(a[0], a[1])]
            if a[2] in o.__class__.__dict__.keys():
                v = type(o.__class__.__dict__[a[2]])
                o.__dict__[argl[2]] = v(a[3])
            else:
                o.__dict__[a[2]] = a[3]
        elif type(eval(a[2])) == dict:
            o = ob["{}.{}".format(a[0], a[1])]
            for y, z in eval(a[2]).items():
                if (y in o.__class__.__dict__.keys() and
                        type(o.__class__.__dict__[y]) in {str, int, float}):
                    v = type(o.__class__.__dict__[y])
                    o.__dict__[y] = v(z)
                else:
                    o.__dict__[y] = z
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
