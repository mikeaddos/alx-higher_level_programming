#!/usr/bin/python3
def search_replace(my_list, search, replace):
    nw_list = list(map(lambda a: replace if a == search else a, my_list))
    return (nw_list)
