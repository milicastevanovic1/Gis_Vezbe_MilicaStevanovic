''' Napisati program koji za unetu vrednost n i k računa broj celobrojnog pojavljivanja broja k u broju
n. Napomena: Ne koristiti aritetički operator ostatka pri deljenju.'''

p=str(input("Unesi broj: "))
q=str(input("Broj za trazenje:  "))

r= p.count(q)
if r==0:
    print (q, "nije nadjen u broju", p)
else:
    print (q, "pojavljuje se u broju", p, r, "puta")