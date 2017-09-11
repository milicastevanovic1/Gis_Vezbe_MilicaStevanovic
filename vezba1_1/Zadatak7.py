p= [ 0 for i in range(4) ]
print ("Unesi 4 broja")
suma = 0
for i in range(4):
    p[i]= int(input())
for i in range(4):
   if p[i]>0:
    suma = suma + p[i]
print ("Uneti brojevi su", p)
print ("Suma pozitivnih brojeva je", suma)