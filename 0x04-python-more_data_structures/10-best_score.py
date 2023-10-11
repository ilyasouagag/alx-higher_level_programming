#!/usr/bin/python3
def best_score(a_dictionary):
    max = 0
    if not a_dictionary:
        return None
    biggest_key = None
    for key in a_dictionary:
        if a_dictionary[key] > max:
            biggest_key = key
            max = a_dictionary[key]
    return biggest_key
