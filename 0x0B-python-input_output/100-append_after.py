#!/usr/bin/python3
"""function that inserts a line of text"""


def append_after(filename="", search_string="", new_string=""):
    """writelines take a list of strings as parameter"""
    with open(filename, 'r', encoding='utf-8') as file:
        final_string = []
        while True:
            line = file.readline()
            if line == "":
                break
            final_string.append(line)
            if search_string in line:
                final_string.append(new_string)
    with open(filename, 'w', encoding='utf-8') as file:
        file.writelines(final_string)
