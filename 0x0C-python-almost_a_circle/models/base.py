#!/usr/bin/python3
"""base class definition file
"""
import json
from os import path

class Base:
    """
    A base class definition having init dunder method
    and a private class attribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
        
    @classmethod
    def reset(cls):
        cls.__nb_objects = 0
    
    @staticmethod
    def to_json_string(list_dictionaries):
        """
        return JSON string representation of list dictionaries

        Args:
            list_dictionaries (list): list of dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """return list from JSON string representation
        
        Args:
            json_string (str): a string representing a dict list
        """
        if not json_string:
            return ''
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        write a JSON representation of list_objs to a file

        Args:
            cls (class): class object
            list_objs (list): list of objects inheriting from Base
        """
        List = []

        if not list_objs:
            list_objs = []
        for obj in list_objs:
            List.append(obj.to_dictionary())

        with open('{}.json'.format(cls.__name__), mode='w', encoding='UTF-8') as f:
            f.write(cls.to_json_string(List))

    @classmethod
    def create(cls, **dictionary):
        """return instance with attributes set

        Args:
            dictionaries (dict): dictionary of elements
                                 to create an instance
        Return:
            a rectangle or square instance, or None
        """
        if cls.__name__ == 'Rectangle':
            r1 = cls(10, 10)
            r1.update(**dictionary)
            return r1
        if cls.__name__ == 'Square':
            s1 = cls(10)
            s1.update(**dictionary)
            return s1
        return None

    @classmethod
    def load_from_file(cls):
        """return list of instances from a file"""
        file = '{}.json'.format(cls.__name__)

        if not path.exists(file):
            return []

        with open(file, mode='r', encoding='UTF-8') as f:
            dict_list = cls.from_json_string(f.read())

        return [cls.create(**Dict) for Dict in dict_list]
        
