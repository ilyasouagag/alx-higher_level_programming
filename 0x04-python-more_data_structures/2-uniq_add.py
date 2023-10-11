#!/usr/bin/python3
def uniq_add(my_list=[]):
    if not my_list:
        return 0
    ls = list(set(my_list))
    somme = sum(ls)
    return somme
