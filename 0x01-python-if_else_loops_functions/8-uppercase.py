#!/usr/bin/python3
def uppercase(str):
    formated_string = ''
    for i in str:
        if i >= 'a' and i <= 'z':
            formated_string += chr(ord(i) - 32)
        else:
            formated_string += i
    print("{}".format(formated_string))
