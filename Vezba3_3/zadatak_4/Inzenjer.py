#!/usr/bin/env python2
# -*- coding: utf-8 -*-


class Inzenjer:
    def __init__(self, ime, prezime, jmbg, licenca):
        self._ime = ime
        self._prezime = prezime
        self._jmbg = jmbg
        self._licenca = licenca

    @property
    def ime(self):
        return self._ime

    @ime.setter
    def ime(self, x):
        self._ime = x

    @property
    def prezime(self):
        return self._prezime

    @prezime.setter
    def prezime(self, x):
        self._prezime = x

    @property
    def jmbg(self):
        return self._jmbg

    @jmbg.setter
    def jmbg(self, x):
        self._jmbg = x

    @property
    def licenca(self):
        return self._licenca

    @licenca.setter
    def licenca(self, x):
        self._licenca = x

    def __str__(self):
        if self.licenca is None:
            l = ' Lice nema licencu,'
        else:
            l = ' Licenca: ' + str(self.licenca)
        return "Ime: %s, Prezime: %s, JMBG: %d," % (self.ime, self.prezime, self.jmbg) + l
