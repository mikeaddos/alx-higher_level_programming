#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    length = len(my_list)

    nw_list = my_list[:]

    if 0 <= idx < length:
        nw_list[idx] = element

    return (nw_list)
