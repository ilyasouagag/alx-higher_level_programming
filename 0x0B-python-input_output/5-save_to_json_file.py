#!/usr/bin/python3
""" function that writes an Object to a text file, using JSON"""
import json


def save_to_json_file(my_obj, filename):
    """ function that writes an Object to a text file, using JSON """
    with open(filename, 'w', encoding='UTF-8') as file:
        json.dump(my_obj, file)
