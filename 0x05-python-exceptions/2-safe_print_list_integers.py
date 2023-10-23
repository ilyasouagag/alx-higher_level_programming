#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    c = 0
    for i in my_list:
        x -= 1
        try:
            print("{:d}".format(i), end='')
            c += 1
        except (TypeError, ValueError):
            pass
        if x == 0:
            break
    print()
    return c
