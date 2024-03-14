import numpy as np


def integrate(f, a, b, N):
    l = (b - a) / N
    k = ((-1/3**0.5) + 1)/2*l
    zasadi = np.linspace(a, b-l, num=N)
    ey = np.linspace(a+l, b, num=N)
    return (b-a)*(np.sum(f(zasadi+k)) + np.sum(f(ey - k)))/(N*2)


def f(x):
    return 1

print(integrate(f, -1, 1, 1))