#!/usr/bin/python3
import sys
length = len(sys.argv) - 1

# ensures operation doesn't occur if file is imported
if __name__ == "__main__":
    # import sys
    # length = len(sys.argv) - 1

    if length == 0:
        print("0 arguments.")
    elif length == 1:
        print("1 argument:\n1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(length))
        # loop the sys argv attribute to print the elements
        for arg in range(1, length + 1):
            print("{}: {}".format(arg, sys.argv[arg]))
