# -*- coding: utf-8 -*-
import numpy as np

height = [1.73, 1.68, 1.71, 1.89, 1.79]
weight = [65.4, 59.2, 63.6, 88.4, 68.7]
np_height = np.array(height)
np_weight = np.array(weight)
print(np_weight / np_height)

a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)
print(a.shape)
a.shape = (3, 2)
print(a)

b = np.arange(15).reshape(3, 5)
print(b)
print(b.shape)
b.reshape(5, 3)
print(b)
print(b.ndim)
