#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    number = 0

    for m in range(x):
        try:
            print("{:d}".format(my_list[m]), end='')
        except TypeError:
            pass
        except ValueError:
            pass
        else:
            number += 1

    print()
    return (number)
