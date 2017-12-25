# -*- coding: utf-8 -*-
# 数组的定义方式
import numpy as np

data1 = np.array([1, 2, 3, 4])
print(data1.dtype)

data2 = np.array([1.0, 2, 3, 4])
print(data2.dtype)

data3 = np.zeros((3, 4))
print(data3)

data4 = np.arange(10, 30, 3, dtype=int)
print(data4)
print(data4.dtype)

data5 = np.linspace(-1.0, 0, 6)
print(data5)

data6 = np.random.normal(2, 0.5, 10000)
print(data6)
