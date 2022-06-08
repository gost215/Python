import math

def z2(x):
    if x < 91:
        return (x**3+x**2+42*x)**5-43*(41*x**3+x*2+50)-((x**6)/87)
    elif 91 <= x < 155:
        return 24*math.sin(x**2+97+x**3)**6+math.atan(x**2)**4
    elif x >=155:
        return x**7+87*math.atan(1+x**3+x)**5+(52*x**2-35-70*x)**6


print('%.2e' %z2(135))
print('%.2e' %z2(159))