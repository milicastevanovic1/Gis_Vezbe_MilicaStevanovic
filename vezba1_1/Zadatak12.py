''' Napisati program koji za unetu cenu proizvoda ispisuje najmanji broj novčanica koje je potrebno
izdvojiti prilikom plaćanja proizvoda. Na raspolaganju su novčanice od 5000, 2000, 1000, 200, 100,
50, 20, 10 i 1 dinar. Napomena: Pretpostaviti da je cena proizvoda pozitivan ceo broj. '''

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#cena = input("Cena proizvoda: ")

def z12(cena):
      n5000 = cena / 5000
      cena %= 5000
      n2000 = cena / 2000
      cena %= 2000
      n1000 = cena / 1000
      cena %= 1000
      n500 = cena / 500
      cena %= 500
      n200 = cena / 200
      cena %= 200
      n100 = cena / 100
      cena %= 100
      n50 = cena / 50
      cena %= 50
      n20 = cena / 20
      cena %= 20
      n10 = cena / 10
      cena %= 10
      n5 = cena / 5
      cena %= 5
      n2 = cena / 2
      cena %= 2
      n1 = cena / 1
      cena %= 1

      print("Broj potrebnih novcanica je "
            "5000-%d, 2000-%d, 1000-%d, 500-%d, 200-%d, 100-%d, 50-%d,"
            "20-%d, 10-%d, 5-%d, 2-%d, 1-%d"
            % (n5000, n2000, n1000, n500, n200, n100, n50, n20, n10, n5, n2, n1,))
