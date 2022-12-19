#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = []
    for elem in my_list:
        if elem != search:
            new.append(elem)
        else:
            new.append(replace)
    return new
