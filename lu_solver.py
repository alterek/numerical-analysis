import numpy as np


float_formatter = "{:.6f}".format
np.set_printoptions(formatter={'float_kind' : float_formatter})


def decompose_to_lu(a):
    n = a.shape[0]
    l = np.zeros((n, n))
    u = np.zeros((n, n))

    for j in range(n):
        for i in range(n):
            if i <= j:
                s = 0
                for k in range(i):
                    s += (l[i][k] * u[k][j])
                u[i][j] = a[i][j] - s
            else:
                s = 0
                for k in range(i):
                    s += (l[i][k] * u[k][j])
                l[i][j] = (a[i][j] - s) / u[j][j]
    return l, u


def solve_lu(l, u, b):
    n = l.shape[0]
    y = np.zeros(n)
    x = np.zeros(n)
    for i in range(n):
        s = 0
        for k in range (i):
            s += l[i][k] * y[k]
        y[i] = b[i] - s
    for i in range(n-1, -1, -1):
        s = 0
        for k in range (i+1, n):
            s += u[i][k] * x[k]
        x[i] = (y[i] - s) / u[i][i]
    return x


A = np.zeros((5, 5))
b = np.zeros((5, 1))

f = open('linear_system.txt')

for i in range(5):
    e = f.readline().split()
    A[i] = e[0:5]
    b[i] = e[5]

f.close()


L, U = decompose_to_lu(A)
x = solve_lu(L, U, b)
print(x)