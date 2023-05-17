#!/usr/bin/python3
def uniq_add(my_list=[]):
    u_list = set(my_list)
    number = 0

    for m in u_list:
        number += m

    return (number)
