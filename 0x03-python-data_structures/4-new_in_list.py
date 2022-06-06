def new_in_list(my_list, idx, element):
    if(idx < 1):
        return my_list
    if(idx > len(my_list) - 1):
        return my_list

    new_list = my_list.copy()
    new_list[idx] = element

    print(new_list)
    print(my_list)
