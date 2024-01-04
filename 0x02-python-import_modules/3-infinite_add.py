#!/usr/bin/python3
import sys
length = len(sys.argv)

# ensures module runs as a command line input only
if __name__ == "__main__":
    total = 0
    # loop to add elements
    for num in range(1, length):
        # cast the argv elements to int then add
        total += int(sys.argv[num])

    # print sum
    print("{}".format(total))
