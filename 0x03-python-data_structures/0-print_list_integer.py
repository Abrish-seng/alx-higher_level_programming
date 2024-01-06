#!/usr/bin/python3
def print_list_integer(my_list=[]):
    count = len(my_list)
    for i in range(0,count):
        print("{:d}" .format(my_list[i]))
