#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    my_dict = a_dictionary.copy()
    for key in my_dict:
        my_dict[key] *= 2
    return my_dict
