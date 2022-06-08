import math

def z4(n):
    if n == 0:
        return (-0.36)
    elif n >=1:
        return 5 * math.atan( 32 * z4(n-1) ** 3 - 22 * z4(n-1) - z4(n-1) ** 2 )**2 + 1 + z4(n-1)


print('%.2e' %z4(4))
print('%.2e' %z4(2))
