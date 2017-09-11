#!/usr/bin/env python2
# -*- coding: utf-8 -*-


def naizmenicno(n1, n2, opcija):
    i = 0
    r = list()
    if len(n1) > len(n2):
        d = len(n1)
    else:
        d = len(n2)
    while i < d:
        if opcija:
            r.append(float(n1[i]))
            r.append(float(n2[i]))
        else:
            r.append(float(n2[i]))
            r.append(float(n1[i]))
        i+=1
    return r

if __name__ == "__main__":
    u1 = raw_input("Elementi prvog niza razdvojeni zarezima ")
    u2 = raw_input("Elementi prvog niza razdvojeni zarezima ")
    n1 = u1.split(",")
    n2 = u2.split(",")
    op = raw_input("p - prvo ide elemet prvog niza, d - prvo ide element drugog niza ")
    if op == 'p':
        o = True
    else:
        o = False
    print (naizmenicno(n1, n2, o))