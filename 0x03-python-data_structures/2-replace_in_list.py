#!/usr/bin/python3
def replace_in_list(my_list, idx, new_element):
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    elif idx >= 0 and idx < len(my_list):
        my_list[idx] = new_element
