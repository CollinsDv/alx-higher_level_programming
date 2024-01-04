#!/usr/bin/python3
import sys
import hidden_4

if __name__ == "__main__":
    for elem in dir(hidden_4):
        if elem.startswith('__'):
            continue
        else:
            print(elem)
