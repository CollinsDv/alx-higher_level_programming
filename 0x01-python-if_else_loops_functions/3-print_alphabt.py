#!/usr/bin/python3
for letter in range(97, 123):
    if letter == ord('q') or letter == ord('e'):
        pass
    else:
        print('{}'.format(chr(letter)), end="")
