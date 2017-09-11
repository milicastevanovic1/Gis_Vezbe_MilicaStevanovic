#!/usr/bin/env python2
# -*- coding: utf-8 -*-


from DMT_Tacka import Tacka
from DMT_Povrs import Povrs

p = Povrs()  # površ je kreirana
while True:
    u = raw_input("Unos tacke (za završetak ukucati 'kraj') ")
    if u == "kraj":
        break
    else:
        t = u.split(",")
        p.dodaj_tacku(Tacka(float(t[0]),float(t[1]),float(t[2])))
print("Unos tačaka završen")
print
p.statistika()
print
print("Određivanje najbliže tačke")
u = raw_input("Uneti broj tačke ")
print ("Najbliža tačka odabranoj je")
p.najbliza_tacka(p.tacke[int(u)]).about()
print("Interpolacija visine")
print
u1 = raw_input("Uneti prvu tačku ")
u2 = raw_input("Uneti drugu tačku ")
d = input("Uneti dužinu ")
print ("Sračunata visina iznosi ")
print(Povrs.interpolacija(p.najbliza_tacka(p.tacke[int(u1)]),p.najbliza_tacka(p.tacke[int(u2)]),d))

