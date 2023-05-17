#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    number = 0
    t_weight = 0

    for tp in my_list:
        number += tp[0] * tp[1]
        t_weight += tp[1]

    return (number / t_weight)
