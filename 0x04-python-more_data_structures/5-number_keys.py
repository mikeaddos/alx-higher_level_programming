#!/usr/bin/python3
def number_keys(a_dictionary):
    number = 0
    keys_list = list(a_dictionary.keys())

    for m in keys_list:
        number += 1

    return (number)
