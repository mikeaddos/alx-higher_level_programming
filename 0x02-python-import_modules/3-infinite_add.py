#!/usr/bin/python3
 import sys

    total = 0
    for m in range(len(sys.argv) - 1):
        total += int(sys.argv[m + 1])
    print("{}".format(total))
