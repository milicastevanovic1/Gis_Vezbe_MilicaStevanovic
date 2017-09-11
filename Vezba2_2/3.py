#!/usr/bin/env python2
# -*- coding: utf-8 -*-


def ska_proiz(v1, v2):
    r = list()
    if len(v1) == len(v2):
        b = 0
        while b < len(v1):
            r.append(float(v1[b]) * float(v2[b]))
            b += 1
    return r

if __name__ == "__main__":
    u1 = raw_input("Uneti komponente vektora 1 odvojene zarezima: ")
    u2 = raw_input("Uneti komponente vektora 2 odvojene zarezima: ")
    v1 = u1.split(",")
    v2 = u2.split(",")
    pr = ska_proiz(v1, v2)
    if len(pr) == 0:
        print("Nije moguće izvršiti skalarni proizvod unetih vektora - nisu iste dimenzije vektora")
    else:
        print(pr)