# -*- coding: utf-8 -*-


# 如果 str1 和 str2 存在最大公约数 str，那么就相当于 str1 和 str2 都是由 str 组成的，那么 str1 + str2 和 str2 + str1 应该是相等的
# 如果不满足，那么不存在最大公约数
#
# 我们可以通过 两个字符串的长度来求得最大公约数的长度
# 比如 str1 = "ABABAB", str2 = "ABAB"
#     len1 = 6         len2 = 4
#     那么最大公约数 str = "AB"
#                  len = 2

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if str1 + str2 != str2 + str1:
            return ""
        return str2[0: self.gcd_str(len(str1), len(str2))]

    def gcd_str(self, a, b):
        if a < b:
            return self.gcd_str(b, a)
        if a % b == 0:
            return b
        return self.gcd_str(b, a % b)
