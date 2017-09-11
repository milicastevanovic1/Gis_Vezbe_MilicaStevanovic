#!/usr/bin/env python2
# -*- coding: utf-8 -*-


from Inzenjer import Inzenjer
from GeodetskiInzenjer import GeodetskiInzenjer
from ElektrotehnickiInzenjer import ElektrotehnickiInzenjer

i1 = Inzenjer('Milica', 'Stevanović', 2407990789524, 1)
i2 = GeodetskiInzenjer('Stanko', 'Marić', 060457, None, 1)
i3 = ElektrotehnickiInzenjer('Mihajlo', 'Tijanic', 1708965747032, 2, 5)
print (i1)
print (i2)
print (i3)