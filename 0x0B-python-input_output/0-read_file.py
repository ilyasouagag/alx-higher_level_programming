#!/usr/bin/python3
"""read a text file and prints it"""


def read_file(filename=""):
    """print it to stdout"""
    with open(filename, 'r', encoding='UTF-8') as file:
        print(file.read(), end="")
