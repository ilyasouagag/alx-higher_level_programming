#!/usr/bin/python3
def magic_string():
    magic_string.iter = getattr(magic_string, 'count', -1) + 1
    return 'BestSchool' + ', BestSchool' * magic_string.iter
