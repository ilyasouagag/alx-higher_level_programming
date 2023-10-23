#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    c = 0
    i = 0
    try:
        while (x > 0):
            if (isinstance(my_list[i], int)):
                num = int(my_list[i])
                print("{:d}".format(num), end='')
                x -= 1
                c += 1
            i += 1
    except IndexError:
        pass
    print()
    return c
