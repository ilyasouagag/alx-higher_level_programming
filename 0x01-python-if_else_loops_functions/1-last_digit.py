#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
pos = number
if pos < 0:
    pos *= -1
last_digit = pos % 10
message = "and is less than 6 and not 0"
if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
elif last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is 0")
else:
    print(f"Last digit of {number} is {last_digit} {message}")
