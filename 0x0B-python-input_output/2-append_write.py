#!/usr/bin/python3
"""Write a function that appends a text file and prints it to stdout"""


def append_write(filename="", text=""):
    """Write a function that appends a text file and prints it to stdout"""
    with open(filename, 'a', encoding='UTF-8') as file:
        return file.write(text)
