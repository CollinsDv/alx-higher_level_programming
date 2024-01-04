#!/usr/bin/python3
import sys
length = len(sys.argv) - 1

# ensures operation doesn't occur if file is imported
if __name__ == "__main__":
    # import sys
    # length = len(sys.argv) - 1

    if length == 0:
        print("{} arguements.".format(length))
    else:
        print("{} arguements:".format(length))
        # loop the sys argv attribute to print the elements
        for arg in range(1, length + 1):
            print("{} : {}".format(arg, sys.argv[arg]))
