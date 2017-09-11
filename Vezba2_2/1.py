x = int(input('unesi broj  '))
def fact(x):
    if x == 1:
        return 1
    else: return x * fact(x-1)
print ('Faktorijal unetog broja je', fact(x))