# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
import numpy as np

mu, sigma = 2, 0.5
v = np.random.normal(mu,sigma,10000)
plt.hist(v, bins=50, normed=1)
plt.show()