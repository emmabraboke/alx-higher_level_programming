def print_reversed_list_integer(my_list=[]):
    lenght = len(my_list) - 1
    while(lenght >= 0):
        print(my_list[lenght])
        lenght -= 1