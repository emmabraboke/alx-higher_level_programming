#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if type(key) != str:
        pass
    else:
        a_dictionary[key] = value
    return a_dictionary
