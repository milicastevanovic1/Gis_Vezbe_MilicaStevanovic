''' Program učitava pet karaktera. Ispisati koliko puta su se pojavile cifre. '''
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
unos = list()
print("Za prekid unosa ukucati 'kraj'")
while 1 == 1:
    k = input("Ukucati element unos ")
    if k == "kraj":
        break
    unos.append(k)
brbrojeva = 0
for i in unos:
    if isinstance(i, ( int, long )):
        brbrojeva += 1
print("Broj unetih brojeva je %d" %brbrojeva)