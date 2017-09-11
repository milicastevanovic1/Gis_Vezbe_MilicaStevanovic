#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import math


class Tacka(object):
    def __init__(self, x, y):
        self._x = x
        self._y = y

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

    @classmethod
    def copy_tacka(cls, t):
        s = cls(t.x, t.y)
        return s

    def x_pomeraj(self, tx):
        self.x += tx

    def y_pomeraj(self, ty):
        self.y += ty

    def rastojanje(self, t):
        return math.sqrt((self.y - t.y)**2 + (self.x - t.x)**2)
