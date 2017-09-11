''' Napisati program koji ispituje da li se data tačka M(xm, ym) nalazi unutar trougla čija su temena
tačke A(x1, y1), B(x2, y2) i C(x3, y3) i ispisuje odgovor DA ili NE.'''

A = [1,1]
B = [6,6]
C = [3,9]

M = [17, 2]

P = abs(A[0]*(B[1]-C[1]) + B[0]*(C[1]-A[1]) + C[0]*(A[0]-B[0]))/2

P1 = abs(A[0] * (B[1] - M[1]) + B[0] * (M[1] - A[1]) + M[0] * (A[0] - B[0])) / 2
P2 = abs(M[0] * (B[1] - C[1]) + B[0] * (C[1] - M[1]) + C[0] * (M[0] - B[0])) / 2
P3 = abs(A[0] * (M[1] - C[1]) + M[0] * (C[1] - A[1]) + C[0] * (A[0] - M[0])) / 2

if P == (P1 + P2 + P3):
 print('tacka M ' , M , "pripada trouglu")
else:
    print('tacka M', M, "ne pripada trouglu")