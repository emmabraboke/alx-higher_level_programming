#!/usr/bin/python3
def search(item1, item2):
    new_set = []
    for i in item1:
        if i not in item2:
            new_set.append(i)
    return new_set


def only_diff_elements(set_1, set_2):
    new_set = search(set_1, set_2) + search(set_2, set_1)
    return new_set
