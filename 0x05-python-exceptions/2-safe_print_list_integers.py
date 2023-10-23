#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    c = 0
    i = 0
    for  i in my_list:
        try:
            print("{:d}".format(i), end='')
            c += 1
            x -= 1
        except (TypeError, ValueError):
            pass
        if x == 0:
            break
    print()
    return c
my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list_integers(my_list, 2)
print("nb_print: {:d}".format(nb_print))

my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
nb_print = safe_print_list_integers(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))

nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))