''' kvadratna jednacina'''

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import math


def kv_jedn(a, b, c):
    d = b ** 2 - 4 * a * c
    if d > 0:
        x1 = (-b + math.sqrt(d)) / float(2 * a)
        x2 = (-b - math.sqrt(d)) / float(2 * a)
    elif d == 0:
        x1 = -b / float(2 * c)
        x2 = x1
    else:
        x1 = complex(-b / float(2 * a), - math.sqrt(abs(d)) / (float(2 * a)))
        x2 = complex(-b / float(2 * a), + math.sqrt(abs(d)) / (float(2 * a)))
    return x1, x2

if __name__ == "__main__":
    unos = raw_input("Uneti parametre A, B, C odvojene zarezima: ")
    par = unos.split(",")
    print (kv_jedn(int(par[0]), int(par[1]), int(par[2])))