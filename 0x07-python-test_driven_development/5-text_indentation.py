#!/usr/bin/python3
def text_indentation(text):
    """function thattake a text and print a new line if char is ? or . or :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    string = ""
    for i in text:
        alert = 0
        string += i
        if i == '\n':
            string = string.rstrip()
            print(string)
            string = ""
        if i in ".?:":
            string = string.strip()
            print(string)
            print()
            string = ""
            alert = 1
    if alert == 0 and not all(n == ' ' for n in string):
        string = string.strip()
        print(string)
