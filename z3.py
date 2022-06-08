import math

def z3(a,m,b):
    e3 = 0
    for i in range(1, b+1):
        e2 = 0
        for j in range(1, m+1):
            e1 = 1
            for c in range(1, a+1):
                e1 *= (c**14+(j**2-11*c**3-79*i)**6+(j**3/28))
            e2 +=e1
        e3 += e2
    return e3


print('%.2e' %z3(6,8,4))
print('%.2e' %z3(3,3,3))