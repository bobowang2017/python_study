# -*- coding: utf-8 -*-
import numpy as np

data = np.arange(10) ** 3
print(data)

data[:6: 2] = -1000
print(data)

print(data[::-1])


