#!/usr/bin/python3

def uniq_add(my_list=[]):
    result = 0
    count = []
    for i in my_list:
        if i not in count:
            count.append(i)
            result += i
    return result
