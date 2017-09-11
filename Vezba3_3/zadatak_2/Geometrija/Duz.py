#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from Tacka import Tacka

class Duz:
    def __init__(self, t1, t2):
        self._t1 = t1
        self._t2 = t2

    @property
    def t1(self):
        return self._t1

    @t1.setter
    def t1(self, x):
        self._t1 = x

    @property
    def t2(self):
        return self._t2

    @t2.setter
    def t2(self, y):
        self._t2 = y

    @classmethod
    def duz_koordinate(cls, x1, y1, x2, y2):
        t1 = Tacka(x1, y1)
        t2 = Tacka(x2, y2)
        d = cls(t1, t2)
        return d

    def duzina(self):
        return self.t1.rastojanje(self.t2)
