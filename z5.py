def main(y, z, x):
    r=0
    n=len(y)
    for i in range(1, n+1):
        r += 71 * (42*z[n-i]**3+x[n-i]+y[i-1]**2)**3
    return 51*r

print('%.2e' % main([0.9, 0.6, 0.24],
                    [-0.33, 0.92, 0.07],
                    [-0.6, -0.03, -0.75]))
print('%.2e' % main([-0.21, 0.95, -0.44],
                    [0.47, 0.64, 0.81],
                    [0.31, 0.67, -0.43]))