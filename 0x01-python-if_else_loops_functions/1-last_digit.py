#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# check value of last digit
if number < 0:
    last_digit = (number * -1) % 10
    last_digit *= 1
else:
    last_digit = number % 10

if last_digit > 5:
    print("Last digit of {} is {} and is greater than 5"
            .format(number, last_digit))
elif last_digit == 0:
    print(f"Last digit of {number} is {0} and is 0")
else:
    print(f"Last digit of {number} is {last_digit}"
            " and is less than 6 and not 0")
