#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from Inzenjer import Inzenjer

class ElektrotehnickiInzenjer (Inzenjer):
    def __init__(self, ime, prezime, jmbg, licenca, br_proj):
        Inzenjer.__init__(self, ime, prezime, jmbg, licenca)
        self._br_proj = br_proj

    @property
    def br_proj(self):
        return self._br_proj

    @br_proj.setter
    def br_proj(self, x):
        self._br_proj = x

    def __str__(self):
        return Inzenjer.__str__(self) + " Broj projekata: " + str(self.br_proj)