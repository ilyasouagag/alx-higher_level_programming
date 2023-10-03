#!/usr/bin/python3
def remove_char_at(str, n):
    copie = ''
    for i in range(len(str)):
        if i != n:
            copie += str[i]
    return copie
