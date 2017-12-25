# -*- coding: utf-8 -*-
import numpy as np

data = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(data)

data1 = data.reshape((2, 4))
print(data1)

# 通过reshape生成的新数组和原始数组公用一个内存，也就是说，假如更改一个数组的
# 元素，另一个数组也将发生改变

data[5] = 888
print(data)
print(data1)