#!/usr/bin/env python2
# -*- coding: utf-8 -*-


def suma_parnih_niza(m):
    sum = 0
    i = 0
    while i < len(m):
        if i%2 ==  1:
            sum += float(m[i])
        i+=1
    return sum

if __name__ == "__main__":
    u = raw_input("Elementi niza razdvojeni zarezima ")
    niz = u.split(",")
    print (suma_parnih_niza(niz))