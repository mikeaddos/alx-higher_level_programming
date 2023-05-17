#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    number = 0
    t_weight = 0

    for tupl in my_list:
        number += tupl[0] * tupl[1]
        t_weight += tupl[1]

    return (num / t_weight)
