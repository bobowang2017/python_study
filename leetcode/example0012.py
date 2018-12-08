# -*- coding: utf-8 -*-
# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > 2 ** 31 - 1 or x < 1 - 2 ** 31:
            return 0
        result = str(x)
        temp = '+'
        if result[0] == '-':
            temp = '-'
            result = result[1:]
        result = result[::-1]
        if temp == '-':
            result = int('-' + result)
        else:
            result = int(result)
        return result


if __name__ == '__main__':
    s = Solution()
    data = s.reverse(1534236469)
    print(data)
