# -*- coding: utf-8 -*-
# 给定一个数组，选定其中的任意一些数字，使得它们相加的和最大，需要注意的是，这些数字中任何两个不能相邻。
# 【1,2,4,7,1,8,3】
import numpy as np


class MaxSum(object):
    def __init__(self):
        self.data = dict()

    def dp_opt(self, arr):
        opt = np.zeros(len(arr))
        opt[0] = arr[0]
        opt[1] = max(arr[0], arr[1])
        for i in range(2, len(arr)):
            A = opt[i - 2] + arr[i]
            B = opt[i - 1]
            opt[i] = max(A, B)
        return opt[len(arr) - 1]


s = MaxSum()
res = s.dp_opt([1, 2, 4, 1, 7, 8, 3])
print(res)
