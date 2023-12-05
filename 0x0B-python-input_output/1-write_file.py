#!/usr/bin/python3
"""Write a function that writess a text file and prints it to stdout"""


def write_file(filename="", text=""):
    """Write a function that writes a text file and prints it to stdout"""
    with open(filename, 'w', encoding='UTF-8') as file:
        return file.write(text)
