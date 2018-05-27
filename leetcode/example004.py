# -*- coding: utf-8 -*-
# 给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。
#
# 注意：
#
# num1 和num2 的长度都小于 5100.
# num1 和num2 都只包含数字 0-9.
# num1 和num2 都不包含任何前导零。
# 你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。


class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num_one = 0
        num_two = 0
        for one in num1:
            num_one = num_one * 10 + int(one)
        for two in num2:
            num_two = num_two * 10 + int(two)
        return str(num_one + num_two)


solution = Solution()
result = solution.addStrings("123456", "8542145")
print(result)
