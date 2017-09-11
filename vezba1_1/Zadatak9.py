'''Napisati program koji za učitani karakter ispisuje uneti karakter i njegov ASCII kod. Ukoliko je uneti
karakter malo (veliko) slovo, ispisati i odgovarajuće veliko (malo) slovo i njegov ASCII kod.'''

from future_builtins import ascii
s = "f"
print ("Uneseni karakter je", s, "njegova ASCII vrednost je '", ord(s))
if s == s.swapcase():
    print(s.lower(), 'njegova ASCII vrednost je', ord(s))
else:
    print(s.swapcase(), 'njegova ASCII vrednost je', ord(s))



