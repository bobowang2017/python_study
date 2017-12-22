# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt

plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
# 指定Y轴标签
plt.ylabel('some numbers')
# 并指定轴域的可视区域
plt.axis([0, 6, 0, 20])
plt.show()
