# -*- coding: utf-8 -*-
# 给定一个字符串，找出不含有重复字符的最长子串的长度。
# 示例：
# 给定 "abcabcbb" ，没有重复字符的最长子串是 "abc" ，那么长度就是3。
# 给定 "bbbbb" ，最长的子串就是 "b" ，长度是1。
# 给定 "pwwkew" ，最长子串是 "wke" ，长度是3。请注意答案必须是一个子串，"pwke" 是 子序列  而不是子串。
# 测试用例 jxdlnaaij 、abcaa、aac、dvdf


class Solution:
    """
    @param: s: a string
    @return: an integer
    """

    def lengthOfLongestSubstring(self, s):
        # write your code here
        res = 0
        if s is None or len(s) == 0:
            return res
        if len(s) == 1:
            return 1
        d = {}
        temp = 0
        start = 0
        for i in range(len(s)):
            if s[i] in d:
                start = d[s[i]] + 1
                d[s[i]] = i
                temp = i - start + 1
                res = max(temp, res)
                print('start=%s, temp=%s, res=%s' % (start, temp, res))
            else:
                d[s[i]] = i
                res = max(i - start, res)
        if len(d) == len(s):
            res = len(s)
        return res


solution = Solution()
result = solution.lengthOfLongestSubstring("jxdlnaaij")
print(result)
