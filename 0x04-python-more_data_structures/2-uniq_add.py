#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq = set(my_list)
    total = 0
    for elem in uniq:
        total += elem
    return total
