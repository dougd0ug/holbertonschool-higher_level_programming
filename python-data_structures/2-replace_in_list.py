#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    new_list = my_list
    if idx < 0:
        return (my_list)
    elif idx >= len(my_list):
        return (my_list)
    elif idx == 0:
        my_list[0] = element
        new_list[0] = element
    else:
        for i in my_list:
            if i == idx:
                my_list[i] = element
                new_list[i] = element
    return (new_list)
