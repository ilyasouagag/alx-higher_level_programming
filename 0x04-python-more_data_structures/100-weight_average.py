#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    sum = 0
    mul = 1
    for row in my_list:
        for i in row:
            mul *= i
        sum += mul
        mul = 1
    print(sum)
    sum2 = 0
    for row in my_list:
        sum2 += row[-1]
    print(sum2)
    return sum / sum2
