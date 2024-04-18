#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_set = set(my_list)
    y = 0
    for i in new_set:
        y += i
    return y
