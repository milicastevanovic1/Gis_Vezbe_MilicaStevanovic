#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import math


class Sfera:
    broj = int()

    @staticmethod
    def br_sfera():
        return Sfera.broj

    def __init__(self):
        self.r = 1
        self.xCentar = 0
        self.yCentar = 0
        self.zCentar = 0

    @classmethod
    def j_sfera(cls):
        s = cls()
        cls.broj += 1
        return s

    @classmethod
    def j_sfera_u_tacki(cls, x, y, z):
        s = cls()
        s.r = 1
        s.xCentar = x
        s.yCentar = y
        s.zCentar = z
        cls.broj += 1
        return s

    @classmethod
    def sfera_u_tacki(cls, r, x, y, z):
        s = cls()
        s.r = r
        s.xCentar = x
        s.yCentar = y
        s.zCentar = z
        cls.broj += 1
        return s

    def zapremina(self):
        v = 4*(self.r**3)*math.pi/3.0
        return v
