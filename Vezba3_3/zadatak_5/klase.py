#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import datetime


class Osoba:
    def __init__(self, ime, prezime, drodj, mrodj, grodj, adresa):
        self._ime = ime
        self._prezime = prezime
        self._rodj = datetime.date(grodj, mrodj, drodj)
        self._adresa = adresa

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
    def rodj(self):
        return self._rodj

    def set_rodj(self, drodj, mrodj, grodj):
        self._rodj = datetime.date(grodj, mrodj, drodj)

    @property
    def adresa(self):
        return self._adresa

    @adresa.setter
    def adresa(self, x):
        self._adresa = x

    def __str__(self):
        return "Ime:%s, Prezime:%s, Datum rođenja:%s, Adresa:%s" % (self.ime, self.prezime, str(self.rodj), self.adresa)


class Zaposlen(Osoba):
    def __init__(self, ime, prezime, drodj, mrodj, grodj, adresa, kompanija, departman):
        Osoba.__init__(self, ime, prezime, drodj, mrodj, grodj, adresa)
        self.kompanija = kompanija
        self.departman = departman
        self.istorija = list()

    def dodaj_istoriju(self, naziv, dp, mp, yp, dk, mk, yk):
        self.istorija.append(Istorija(naziv, dp, mp, yp, dk, mk, yk))

    def __str__(self):
        ist = ""
        for i in self.istorija:
            ist += "\nNaziv zaposlenja: %s, Od: %s, Do: %s" % (i.naziv, str(i.dp), str(i.dk))
        return (Osoba.__str__(self) + " Kompanija: %s, Departman: %s" % (self.kompanija, self.departman)
                + "\nPrethnodna zaposlenja" + ist)

    def radni_staz(self):
        ukupno = 0
        for i in self.istorija:
            ukupno += (i.dk - i.dp).days
        ukupno /= 30
        return "Radni staž zaposlenog je %d meseci" % ukupno


class Istorija:
    def __init__(self,  naziv, dp, mp, yp, dk, mk, yk):
        self.naziv = naziv
        self.dp = datetime.date(yp, mp, dp)
        self.dk = datetime.date(yk, mk, dk)


class Djak(Osoba):
    def __init__(self, ime, prezime, drodj, mrodj, grodj, adresa, skola, du, mu, gu, razred):
        Osoba.__init__(self, ime, prezime, drodj, mrodj, grodj, adresa)
        self.skola = skola
        self.upis = datetime.date(gu, mu, du)
        self.razred = razred

    def __str__(self):
        return Osoba.__str__(self) + " Škola:%s, Datum upisa:%s, Razred:%d" % (self.skola, str(self.upis), self.razred)

    def inf(self):
        ob = "NE"
        if datetime.date.today() > self.upis + datetime.timedelta(days=(self.razred * 365.25 )):
            ob = "DA"
        return "Ime: %s, Prezime: %s, Razred: %s, Ponavljao razred: %s" % (self.ime, self.prezime, str(self.rodj), ob)
