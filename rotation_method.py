import numpy as np


float_formatter = "{:.6f}".format
np.set_printoptions(formatter={'float_kind' : float_formatter})


def solve_with_rotation(m):
    n = m.shape[0]
    for i in range(n-1):
        for j in range(i + 1, n):
            den = (m[i, i]**2 + m[j, i]**2) ** .5
            c = m[i, i] / den
            s = m[j, i] / den
            for z in range (n+1):
                A1 = m[i][z]
                t = m[j][z]
                m[i][z] = c * A1 + s * t
                m[j][z] = -s * A1 + c * t

    x = np.zeros(n)
    for k in range(n - 1, -1, -1):
        t = m[k][n]
        for z in range (k+1, n):
            t -= m[k][z] * x[z]
        t /= m[k][k]
        x[k] = t
    return x


m = np.zeros((5,6))
f = open('linear_system.txt')
for i in range(5):
    e = f.readline().split()
    m[i] = e
f.close()


x = solve_with_rotation(m)
print(x)