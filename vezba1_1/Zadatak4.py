''' Sa standardnog ulaza se unose dva četvorocifrena broja. Napisati program koji na standardni izlaz
ispisuje sumu cifara drugog broja, a potom i razliku zbira cifara prvog broja na parnim i neparnim
pozicijama.
 '''

a=4386
b=7125


m=(b//1000)
n=(((b-(10*((b/10)%10))-(b%10))%1000)/100)
p=((b/10)%10)
q=(b%10)
print ("Suma cifara u drugom broju je:", m+n+p+q)

s=(a//1000)
q=(((a-(10*((a/10)%10))-(a%10))%1000)/100)
x=((a/10)%10)
y=(a%10)
print ("Razlika suma cifara na neparnim i parnim pozicijama je:", (q+y)-(s+x))
