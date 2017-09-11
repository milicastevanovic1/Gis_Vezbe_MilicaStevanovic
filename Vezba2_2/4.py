#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import math


def int_vekt(v1):
    s = 0
    for k in v1:
        s += float(k)**2
    return math.sqrt(s)

if __name__ == "__main__":
    u = raw_input("Uneti komponente vektora odvojene zarezima: ")
    v = u.split(",")
    print(int_vekt(v))