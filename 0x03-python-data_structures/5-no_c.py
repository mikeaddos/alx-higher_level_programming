#!/usr/bin/python3
def no_c(my_string):
    length = len(my_string)

    k = 0

    nw_string = my_string[:]

    for m in range(length):
        if (my_string[m] == 'c' or my_string[m] == 'C'):
            nw_string = nw_string[:(m - k)] + my_string[(m + 1):]
            k += 1

    return (nw_string)
