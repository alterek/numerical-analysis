import numpy as np


float_formatter = "{:.6f}".format
np.set_printoptions(formatter={'float_kind' : float_formatter})


def solver(a, b, c, d):
    n = len(d)
    c_new = c.copy()
    d_new = d.copy()

    c_new[0] = c[0] / b[0]
    d_new[0] = d[0] / b[0]

    for i in range(1, n):
        den = b[i] - a[i-1] * c_new[i-1]
        if i != n-1:
            c_new[i] = c[i] / den
        d_new[i] = (d[i] - a[i-1] * d_new[i-1]) / den

    x = np.zeros(n)
    x[-1] = d_new[-1]

    for i in range(n - 2, -1, -1):
        x[i] = d_new[i] - c_new[i] * x[i+1]
    return x


a = np.array([0.702841, -5.30564, -9.68688, -5.33677])
b = np.array([-4.87472, -8.53938, 5.55101, 7.78191, -7.62505])
c = np.array([-7.39494, 2.64992, 6.78701, 6.72597])
d = np.array([9.67528, 0.448927, 5.21531, -6.8926, -8.41304])

float_formatter = "{:.6f}".format
np.set_printoptions(formatter={'float_kind' : float_formatter})


x = solver(a, b, c, d)
print(x)