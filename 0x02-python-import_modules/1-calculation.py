#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

# initialize arguements
a = 10
b = 5

# call functions with calculation operations
if __name__ == "__main__":
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
