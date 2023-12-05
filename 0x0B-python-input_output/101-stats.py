#!/usr/bin/python3
"""script that reads stdin line by line and calcuates"""
import sys

size = 0
status = {"200": 0, "301": 0, "400": 0, "401": 0,
          "403": 0, "404": 0, "405": 0, "500": 0}
i = 0
try:
    for line in sys.stdin:
        args = line.split()
        if len(args) >= 2:
            a = i
            if args[-2] in status:
                status[args[-2]] += 1
                i += 1
            try:
                size += int(args[-1])
                if a == i:
                    i += 1
            except FileNotFoundError:
                if a == i:
                    continue
        if i % 10 == 0:
            print("File size: {:d}".format(size))
            for key, value in sorted(status.items()):
                if value:
                    print("{:s}: {:d}".format(key, value))
    print("File size: {:d}".format(size))
    for key, value in sorted(status.items()):
        if value:
            print("{:s}: {:d}".format(key, value))

except KeyboardInterrupt:
    print("File size: {:d}".format(size))
    for key, value in sorted(status.items()):
        if value:
            print("{:s}: {:d}".format(key, value))
