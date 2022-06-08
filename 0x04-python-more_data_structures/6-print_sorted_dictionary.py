#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dict_list = sorted(a_dictionary)
    for i in dict_list:
        print("{:s}: {}".format(i, a_dictionary[i]))
