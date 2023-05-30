#!/usr/bin/python3
def magic_calculation(a, b):
    mc_result = 0
    for m in range(1, 3):
        try:
            if m > a:
                raise Exception('Too far')
            mc_result += a ** b / m
        except Exception:
            mc_result = b + a
            break
    return mc_result
