#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        last_d = number % 10
    else:
        last_d = number % -10
        last_d *= -1

    print("{:d}".format(last_d), end='')
    return (last_d)
