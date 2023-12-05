#!/usr/bin/python3
"""function that inserts a line of text"""


def append_after(filename="", search_string="", new_string=""):
    """this function uses writelines that takes from a list"""
    with open(filename, 'r', encoding='UTF-8') as file:
        final_string = []
        while True:
            for line in file:
                if line == "":
                    break
                final_string.append(line)
                if search_string in line:
                    final_string.append(search_string)
    with open(filename, 'w', encoding='UTF-8') as file:
        file.writelines(final_string)
