#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return 0
    sum_1 = 0
    sum_2 = 0
    for i, j in my_list:

        sum_1 += i * j
        sum_2 += j

    average = sum_1 / sum_2
    return average
