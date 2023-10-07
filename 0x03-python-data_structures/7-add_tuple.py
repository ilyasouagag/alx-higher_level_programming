#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0 and len(tuple_b) ==0:
        return ()
    if len(tuple_a) == 0:
        return tuple_b[:2]
    if len(tuple_b) == 0:
        return tuple_a[:2]
    if len(tuple_a) == 1:
        return tuple_a[0] + tuple_b[0], tuple_b[1]
    if len(tuple_b) == 1:
        return tuple_a[0] + tuple_b[0], tuple_a[1]
    return tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)  # Output: (89, 100)

print(add_tuple(tuple_a, (1, )))  # Output: (2, 89)
print(add_tuple(tuple_a, ())) 