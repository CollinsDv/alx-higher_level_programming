#!/usr/bin/python3
def no_c(my_string):
    char_list = [letter for letter in my_string if letter.lower() != 'c']
    my_string = ''.join(char_list)

    return my_string
