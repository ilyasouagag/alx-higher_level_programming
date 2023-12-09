#!/usr/bin/python3
import json


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if not id:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionnaries):
        if not list_dictionnaries or list_dictionnaries is None:
            return "[]"
        return json.dumps(list_dictionnaries)

    @classmethod
    def save_to_file(cls, list_objs):
        list_dict = []
        file_name = cls.__name__ + ".json"
        with open(file_name, 'w') as file:
            if not list_objs:
                file.write("[]")
            for a in list_objs:
                list_dict.append(a.to_dictionary())
            file.write(Base.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        if not json_string or json_string is None:
            return "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionnary):
        if dictionnary and dictionnary != {}:
            if cls.__name__ == "Rectangle":
                instance = cls(10, 2, 3)
            else:
                instance = cls(5)
            instance.update(**dictionnary)
        return instance
    @classmethod
    def load_from_file(cls):
        loaded = []
        file_name= cls.__name__ + ".json"
        try:
            with open(file_name,'r') as file:
                list_dict = Base.from_json_string(file.read())
                for i in list_dict:
                    loaded.append(cls.create(**i))
            return loaded
        except OSError:
            return []
