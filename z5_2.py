import math

def z5_1(z,x):
    r=0
    n = len(z)
    for i in range (1, n+1):
        r += (25 * x[n-i] - 37*z[math.ceil(i/4)-1]**3-1)**3
    return 59*r

print('%.2e' % z5_1([-0.01, -0.38],
                     [0.83, -0.05]))