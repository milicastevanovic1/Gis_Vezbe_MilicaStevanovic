#!/usr/bin/env python2
# -*- coding: utf-8 -*-


def pro_el_niza(m):
    p = 1
    i = 0
    while i < len(m):
        p *= float(m[i])
        i+=1
    return p

if __name__ == "__main__":
    u = raw_input("Elementi niza razdvojeni zarezima ")
    niz = u.split(",")
    print (pro_el_niza(niz))