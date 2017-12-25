# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return np.sin(x)


def c(x):
    return np.cos(x)


x = np.arange(-9.5, 9.5, 0.1)
plt.plot(x, f(x))
plt.plot(x, c(x), color='y')
plt.axhline(color='r')
plt.axvline(color='r')
plt.axis([-9.5, 9.5, -1, 1])
plt.show()
