#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from Geometrija.Tacka import Tacka
from Geometrija.Duz import Duz

up = raw_input("Uneti X i Y koord. početne tačke, odvojene zarezima ")
uk = raw_input("Uneti X i Y koord. krajnje tačke, odvojene zarezima ")
kt1 = up.split(",")
kt2 = uk.split(",")

t1 = Tacka(float(kt1[0]), float(kt1[0]))
t2 = Tacka(float(kt2[0]), float(kt2[0]))
d1 = Duz(t1, t2)
d2 = Duz(Tacka(100, 100), Tacka(200,200))
print ("Kreirana je duž d1, dužine %f" %d1.duzina())
print ("Kreirana je duž d2, dužine %f" %d2.duzina())

utr = raw_input("Uneti X i Y koord. translacije  krajnje tačke duži ")
tr = utr.split(",")
d1.t2.x = float(tr[0])
d1.t2.y = float(tr[1])
print ("Kreirana je duž d3, dužine %f" %d1.duzina())