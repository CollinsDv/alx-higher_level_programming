#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# check value of last digit
if number % 10 > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, number % 10))
elif number % 10 == 0:
    print(f"Last digit of {number} is {0} and is 0")
else:
    print(f"Last digit of {number} is {number % 10} and is less than 6 and not 0")
