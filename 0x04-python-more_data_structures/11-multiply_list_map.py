#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    copy_list = my_list[:]
    return list(map(lambda x: x * number, copy_list))
