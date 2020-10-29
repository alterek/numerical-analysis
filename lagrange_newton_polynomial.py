import numpy as np
# import matplotlib.pyplot as plt


def coef_n(x, y):
    n = len(x)
    a = [i for i in y]
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            a[i] = float(a[i] - a[i - 1]) / float(x[i] - x[i - j])
    return a


def eval_n(a, x, r):
    n = len(a) - 1
    temp = a[n]
    for i in range(n - 1, -1, -1):
        temp = temp * (r - x[i]) + a[i]
    return temp


def print_n(a, x):
    s = ''
    for i in range(len(a)):
        s += str("%.4f" % (a[i]))
        for j in range(i):
            if x[j] <= 0:
                s += '(x+{})'.format(abs(x[j]))
            else:
                s += '(x-{})'.format(x[j])
        if i != len(a) - 1:
            if a[i + 1] > 0:
                s += '+'
                s += '\n'
                s += '+'
            else:
                s += '-'
                s += '\n'
    print(s)


def coef_l(x, y):
    temp = [1.] * len(x)
    k = 0
    for j in x:
        for i in x:
            if i != j:
                temp[k] *= (j - i)
        temp[k] = y[k] / temp[k]
        k += 1
    return temp


def eval_l(a, x, r):
    s = 0
    k = 0
    for j in x:
        t = 1
        for i in x:
            if i != j:
                t *= (r - i)
        t *= a[k]
        k += 1
        s += t
    return s


def print_l(a, x):
    s = ''
    for i in range(len(a)):
        for j in range(len(x)):
            if i != j:
                if x[j] <= 0:
                    s += '(x+{})'.format(abs(x[j]))
                else:
                    s += '(x-{})'.format(x[j])
        if a[i] > 0:
            s += str("(1/%.4f)" % (1 / a[i]))
        else:
            s += str("(-1/%.4f)" % (1 / abs(a[i])))
        if i != len(a) - 1:
            s += '+' + '\n' + '+'
    print(s)


def main():
    float_formatter = "{:.2f}".format
    np.set_printoptions(formatter={'float_kind': float_formatter})

    x = [-2, -1, 0, 1, 2, 3, 4]
    y = [-3.73, 6.12, 7.73, -7.96, -6.31, 8.85, 1.65]
    # y = [6.10, 1.55, -1.71, -5.08, 6.19, -6.37, 3.28]

    print(np.array(coef_n(x, y)))
    print()
    print(1 / np.array(coef_l(x, y)))
    print()

    r = -1.3
    print('{:.6f}'.format(eval_n(coef_n(x, y), x, r)))
    print()
    r = 1.75
    print('{:.6f}'.format(eval_n(coef_n(x, y), x, r)))
    print()

    print_n(np.array(coef_n(x, y)), x)
    print()
    print_l(np.array(coef_l(x, y)), x)
    print()
    # x_new = np.linspace(np.min(x), np.max(x), 100)
    # y_new = [eval_n(coef_n(x, y), x, i) for i in x_new]
    # plt.plot(x_new, y_new)
    # plt.grid(True)
    # plt.show()


if __name__ == "__main__":
    main()
