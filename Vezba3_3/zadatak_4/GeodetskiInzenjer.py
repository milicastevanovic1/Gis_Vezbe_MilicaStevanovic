#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from Inzenjer import Inzenjer


class GeodetskiInzenjer (Inzenjer):
    def __init__(self, ime, prezime, jmbg, licenca, staz):
        Inzenjer.__init__(self, ime, prezime, jmbg, licenca)
        self._staz = staz

    @property
    def staz(self):
        return self._staz

    @staz.setter
    def staz(self, x):
        self._staz = x

    def __str__(self):
        return Inzenjer.__str__(self) + ' Staz: ' + str(self.staz)
