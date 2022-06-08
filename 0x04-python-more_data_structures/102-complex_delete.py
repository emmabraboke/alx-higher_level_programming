#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys = []
    for i in a_dictionary:
        if a_dictionary[i] == value:
            if i not in keys:
                keys.append(i)
        print(keys)

    for j in keys:
        del a_dictionary[j]

    return a_dictionary
