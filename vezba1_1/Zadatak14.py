''' Napisati program koji za uneti ceo broj računa razliku suma cifara koje se nalaze na parnim i
neparnim pozicijama u zapisu broja.'''

p = str(input("Unesi broj: "))
i=0
parni=0
neparni=0
for i in range(0,len(p),2):
    neparni = neparni + int(p[i])
for i in range(1,len(p),2):
    parni = parni + int(p[i])

print ('Suma brojeva na parnim pozicijama je', parni, 'Suma brojeva na neparnim pozicijama je', neparni, 'a razlika je:', parni-neparni)