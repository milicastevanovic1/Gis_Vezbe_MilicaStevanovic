#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from Sfera import Sfera

print(Sfera.br_sfera())

jedinicna_sfera = Sfera.j_sfera()
sfera = Sfera.sfera_u_tacki(4.0, 0, 0, 0)
globus = Sfera.sfera_u_tacki(12, 10, 10, 10)
bilijarska_lopta = Sfera.j_sfera_u_tacki(10, 10, 0)

print (Sfera.br_sfera())

print(sfera.zapremina())
print(globus.zapremina())
print(bilijarska_lopta.zapremina())
print(jedinicna_sfera.zapremina())
