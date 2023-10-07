#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a , b = tuple_a[:2] if len(tuple_a) >= 2 else (tuple_a[0] if len(tuple_a) == 1 else 0, 0)
    c , d = tuple_b[:2] if len(tuple_b) >= 2 else (tuple_b[0] if len(tuple_b) == 1 else 0, 0)
    return a + c, b + d
tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))