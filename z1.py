import math

def z1(y,z,x):
    e1= (y**3-z**2-89)**5 - (1-52 * x ** 2)**6
    e2= 71 * (42*z**3+x+y**2)**3 +z**5
    e3= math.sqrt(88*(abs(y-z**2-x**3))**6)
    return e1/e2 +e3


print('%.2e' %z1(0.26, 0.51, 0.92))