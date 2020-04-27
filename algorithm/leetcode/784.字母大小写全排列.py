# -*- coding: utf-8 -*-
# 给定一个字符串S，通过将字符串S中的每个字母转变大小写，我们可以获得一个新的字符串。返回所有可能得到的字符串集合。
# 示例:
# 输入: S = "a1b2"
# 输出: ["a1b2", "a1B2", "A1b2", "A1B2"]
#
# 输入: S = "3z4"
# 输出: ["3z4", "3Z4"]
#
# 输入: S = "12345"
# 输出: ["12345"]
# 注意：
# S 的长度不超过12。
# S 仅由数字和字母组成。


class Solution(object):
    def __init__(self):
        self.result = set()

    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        self.display(S, "", 0)
        return list(self.result)

    def display(self, S, _s, start):
        if start > len(S) - 1:
            # print(_s)
            self.result.add(_s)
            return
        temp = S[start]
        if ord('a') <= ord(temp) <= ord('z'):
            self.display(S, _s + chr(ord(temp) - ord('a') + ord('A')), start + 1)
        elif ord('A') <= ord(temp) <= ord('Z'):
            self.display(S, _s + chr(ord(temp) - ord('A') + ord('a')), start + 1)
        self.display(S, _s + temp, start + 1)


s = Solution()
res = s.letterCasePermutation("12345")
print(res)
