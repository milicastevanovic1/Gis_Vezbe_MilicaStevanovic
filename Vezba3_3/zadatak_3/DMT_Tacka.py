#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import math

class Tacka(object):
    rnd = 1

    def __init__(self, x, y, h):
        self._kod = Tacka.rnd
        self._x = x
        self._y = y
        self._h = h
        Tacka.rnd += 1

    @property
    def kod(self):
        return self._kod

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        self._y = y

    @property
    def h(self):
        return self._h

    @h.setter
    def h(self, h):
        self._h = h

    def rastojanje(self, t):
        return math.sqrt((self.y - t.y)**2 + (self.x - t.x)**2)

    def about(self):
        print("ID - %d ... X = %.2f, Y = %.2f, H = %.2f" % (self.kod, self.x, self.y, self.h))
