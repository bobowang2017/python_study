# -*- coding: utf-8 -*-
# 给定一个 32 位有符号整数，将整数中的数字进行反转。
# 示例 1:
# 输入: 123
# 输出: 321
#  示例 2:
# 输入: -123
# 输出: -321
# 示例 3:
# 输入: 120
# 输出: 21
# 注意:
# 假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−2~31,  2~31 − 1]。根据这个假设，如果反转后的整数溢出，则返回 0。


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < pow(-2, 31) or x > pow(2, 31) - 1:
            return 0
        return int(str(abs(x))[::-1]) if x > 0 else 0 - int(str(abs(x))[::-1])


solution = Solution()
result = solution.reverse(1534236469)
print(result)
print(pow(2, 31) - 1)
