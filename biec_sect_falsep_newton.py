from math import sqrt, tan
import numpy as np
import pandas as pd

pd.set_option('display.float_format', '{:.6f}'.format)


eps = 0.0001


def f(x):
    y = sqrt(25 - x * x) - tan(x) - 1
    return y


def der_f(x):
    y = -x / sqrt(25 - x * x) - tan(x) * tan(x) - 1
    return y


def biec():
    n = 0
    x0 = 0.8
    x1 = 1.4
    f0 = f(x0)
    f1 = f(x1)
    delx = x1 - x0
    df = pd.DataFrame(columns = ['x0', 'f0', 'x1', 'f1', 'delx'])
    while delx > eps:
        df.loc[n] = [x0, f0, x1, f1, delx]
        xm = 0.5 * (x0 + x1)
        n += 1
        fm = f(xm)
        if (f0 * fm > 0):
            x0 = xm
            f0 = fm
        else:
            x1 = xm
            f1 = fm
        delx = abs(x1 - x0)
    df.loc[n] = [x0, f0, x1, f1, delx]
    print(df)


def sect():
    n = 0
    x0 = 0.8
    x1 = 1.4
    f0 = f(x0)
    f1 = f(x1)
    delx = x1 - x0
    df = pd.DataFrame(columns = ['x0', 'f0', 'x1', 'f1', 'delx'])
    while delx > eps:
        df.loc[n] = [x0, f0, x1, f1, delx]
        xm = x1 * f0 / (f0 - f1) + x0 * f1 / (f1 - f0)
        n += 1
        fm = f(xm)
        x0 = x1
        f0 = f1
        x1 = xm
        f1 = fm
        delx = abs(x1 - x0)
    df.loc[n] = [x0, f0, x1, f1, delx]
    print(df)


def falsep():
    n = 0
    x0 = 0.8
    x1 = 1.4
    f0 = f(x0)
    f1 = f(x1)
    delx = x1 - x0
    df = pd.DataFrame(columns = ['x0', 'f0', 'x1', 'f1', 'delx'])
    while delx > eps:
        df.loc[n] = [x0, f0, x1, f1, delx]
        xm = x1 * f0 / (f0 - f1) + x0 * f1 / (f1 - f0)
        n += 1
        fm = f(xm)
        if (f0 * fm > 0):
            delx = xm - x0
            x0 = xm
            f0 = fm
        else:
            delx = x1 - xm
            x1 = xm
            f1 = fm
    df.loc[n] = [x0, f0, x1, f1, delx]
    print(df)


def newton():
    n = 0
    x0 = 1.4
    delx = 2 * eps
    df = pd.DataFrame(columns=['x0', 'f0', 'df0', 'x1', 'delx'])
    while delx > eps:
        f0 = f(x0)
        df0 = der_f(x0)
        x1 = x0 - f0 / df0
        delx = abs(x1 - x0)
        df.loc[n] = [x0, f0, df0, x1, delx]
        x0 = x1
        n += 1
    print(df)


biec()
sect()
falsep()
newton()