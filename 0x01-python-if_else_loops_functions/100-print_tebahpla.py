#!/usr/bin/python3
for i in range(122, 96, -1):
    if i % 2 != 0:
        z = chr(i-32)
    else:
        z = chr(i)
    print("{:s}".format(z), end="")
