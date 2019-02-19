# -*- coding: utf-8 -*-
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

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
        if result < -pow(2, 31) or result > pow(2, 31) - 1:
            return 0
        return result


if __name__ == '__main__':
    s = Solution()
    data = s.reverse(1534236469)
    print(data)
