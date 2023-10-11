#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return None
    total = 0
    prev = 0
    dictio = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in range(len(roman_string)-1, -1, -1):
        a = roman_string[i]
        val = dictio[a]
        if val < prev:
            total -= val
        else:
            total += val
        prev = val
    return total
