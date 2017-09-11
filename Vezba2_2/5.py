#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import numpy


def pro_matrica(a, b):
    return numpy.dot(a, b)

if __name__ == "__main__":
    u1 = raw_input("Matrica A (elementi razdvojeni ',' a vrste ';') ") # npr. 4,2,3;2,1,4;1,1,1
    u2 = raw_input("Matrica B (elementi razdvojeni ',' a vrste ';') ")
    m1 = numpy.matrix(u1)
    m2 = numpy.matrix(u2)
    print (pro_matrica(m1, m2))