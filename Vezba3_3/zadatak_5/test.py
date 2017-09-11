#!/usr/bin/env python2
# -*- coding: utf-8 -*-


from klase import Osoba
from klase import Zaposlen
from klase import Djak

osoba1 = Osoba('Milica', 'Stevanović', 24, 7, 1990, 'Durmitorska 2')
z1 = Zaposlen('Milica', 'Stevanović', 24, 7, 1990, 'Durmitorska 2' ,"NisJugopetrol", 'Prodaja')
z1.dodaj_istoriju("Menadzer", 1, 1, 2001, 5, 5, 2002)
z1.dodaj_istoriju("Marketing menadzer", 5, 5, 2002, 1, 1, 2005,)
print z1
print z1.radni_staz()
print
u1 = Djak('Milan', 'Stosic', 17, 05, 1999, 'Lomina 4','Dusko Radovic', 1, 9, 2012, 7)
print u1.inf()
print u1
