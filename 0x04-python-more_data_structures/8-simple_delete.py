#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if type(key) != str or key not in a_dictionary:
        pass
    else:
        del a_dictionary[key]
    return a_dictionary
