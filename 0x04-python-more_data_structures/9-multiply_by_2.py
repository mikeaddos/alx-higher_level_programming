#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    keys_list = list(new_dict.keys())

    for m in keys_list:
        new_dict[m] *= 2

    return (new_dict)
