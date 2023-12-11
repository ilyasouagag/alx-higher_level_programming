#!/usr/bin/python3
"""create the Base class"""
import json
import csv
import turtle


class Base:
    """class Baase that contain all methods"""
    __nb_objects = 0

    def __init__(self, id=None):
        """create instances from base class"""
        if not id:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionnaries):
        """returns the JSON string representation of list_dictionaries"""
        if not list_dictionnaries or list_dictionnaries is None:
            return "[]"
        return json.dumps(list_dictionnaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """class method save str to file"""
        f = cls.__name__+".json"
        with open(f, "w") as json_f:
            if not list_objs:
                json_f.write("[]")
            else:
                dicts = [num.to_dictionary() for num in list_objs]
                json_f.write(Base.to_json_string(dicts))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if not json_string or json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionnary):
        """returns an instance with all attributes already set"""
        if dictionnary and dictionnary != {}:
            if cls.__name__ == "Rectangle":
                instance = cls(1, 1)
            else:
                instance = cls(1)
            instance.update(**dictionnary)
        return instance

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        loaded = []
        file_name = cls.__name__ + ".json"
        try:
            with open(file_name, 'r') as file:
                list_dict = Base.from_json_string(file.read())
                for i in list_dict:
                    loaded.append(cls.create(**i))
            return loaded
        except OSError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes in CSV"""
        file_name = cls.__name__ + ".csv"
        with open(file_name, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """deserializes in CSV"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ opens a window and draws all the Rectangles and Squares"""
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
