# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return np.sin(x)


x = np.arange(-10, 10, 0.1)
plt.plot(x, f(x))
plt.axis([-10, 10, -1, 1])
plt.show()
