#!/usr/bin/python3

def element_at(my_list, idx):
    if(idx<1):
        return None
    if(idx>len(my_list)-1):
        return None
    print("Element at index {:d} is {}".format(idx, my_list[idx]))
