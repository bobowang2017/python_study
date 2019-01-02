# -*- coding: utf-8 -*-
# 实现 pow(x, n) ，即计算 x 的 n 次幂函数。


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        temp = x if n >= 0 else 1 / x
        n = n if n >= 0 else -n
        result = 1
        for i in range(n):
            result = result * temp
        return result


if __name__ == '__main__':
    s = Solution()
    # data = s.myPow(1.00001, 123456)
    # data = s.myPow(10, -3)
    data = s.myPow(0.00001, 2147483647)
    print(data)
