# 给定一个只包含非负整数的数组，从中找出任意个数字，使得数字的和等于S。
# 如果存在这样的情况返回true，否则返回false。
# 例如：arr = 【3,34,4,12,5,2】 ，找出其中任意个数，使得和为9。
import numpy as np


class EqualSum(object):

    def dp_opt(self, arr, i , _sum):
        if i == 0:
            return False
        if arr[i] == _sum:
            return True
        if arr[i] > _sum:
            return self.dp_opt(arr, i-1, _sum)
        else:
            A = self.dp_opt(arr, i-1, _sum - arr[i])
            B = self.dp_opt(arr, i-1, _sum)
        return A or B


s = EqualSum()
res = s.dp_opt([1, 2, 4, 1, 7, 8, 3], 6, 9)
print(res)
