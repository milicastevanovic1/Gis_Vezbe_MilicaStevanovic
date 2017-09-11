#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import os

class Povrs:
    def __init__(self):
        self._tacke = dict()
        self._br_tacaka = 0
        self._korisnik = os.environ.get("USERNAME")

    @property
    def korisnik(self):
        return self._korisnik

    @property
    def tacke(self):
        return self._tacke

    @property
    def br_tacaka(self):
        return self._br_tacaka

    @br_tacaka.setter
    def br_tacaka(self, x):
        self._br_tacaka = x

    def dodaj_tacku(self, t):
        self.tacke[t.kod] = t
        self.br_tacaka += 1

    def srednja_vrednost(self):
        s = 0
        for i in self.tacke.itervalues():
            s += i.h
        return s/self.br_tacaka

    def min_x(self):
        minx = float("inf")
        for i in self.tacke.itervalues():
            if i.x < minx:
                minx = i.x
        return minx

    def min_y(self):
        miny = float("inf")
        for i in self.tacke.itervalues():
            if i.y < miny:
                miny = i.y
        return miny

    def max_x(self):
        maxx = - float("inf")
        for i in self.tacke.itervalues():
            if i.x > maxx:
                maxx = i.x
        return maxx

    def max_y(self):
        maxy = - float("inf")
        for i in self.tacke.itervalues():
            if i.y > maxy:
                maxy = i.y
        return maxy

    def najbliza_tacka(self, t):
        skup = self.tacke.copy()
        del skup[t.kod]
        mind = float("inf")
        tac = t.kod
        for i in skup.itervalues():
            if i.rastojanje(t) < mind:
                mind = i.rastojanje(t)
                tac = i.kod
        return self.tacke[tac]

    @staticmethod
    def interpolacija(t1, t2, d):
        r = t1.rastojanje(t2)
        if d > r:
            return None
        elif d > r:
            return (t2.h * (r - d) + t1.h * d) / r
        else:
            return (t1.h * (r - d) + t2.h * d) / r

    def statistika(self):
        print ("Broj tačaka površi je %d" % self.br_tacaka)
        print ("Srednja vrednost površi iznosi: %4.f" %self.srednja_vrednost())
        print ("Minimalni obuhvatni pravougaonik površi")
        print ("Xmax = %.2f" % self.max_x())
        print ("Ymax = %.2f" % self.max_y())
        print ("Xmin = %.2f" % self.min_x())
        print ("Ymin = %.2f" % self.min_y())

