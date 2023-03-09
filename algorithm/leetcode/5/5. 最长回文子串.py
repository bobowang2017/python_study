# -*- coding: utf-8 -*-
class Solution(object):
    def longestPalindrome(self, s):
        if s == "":
            return s
        length = len(s)
        dp = [[0 for _ in range(length)] for _ in range(length)]
        left = 0
        right = 0
        for i in range(length):
            dp[i][i] = True
        for i in range(length-2, -1, -1):
            for j in range(i + 1, length):
                dp[i][j] = s[i] == s[j] and (j - i < 3 or dp[i + 1][j - 1])
                if dp[i][j] and right - left < j - i:
                    left, right = i, j
        return s[left:right + 1]


print(Solution().longestPalindrome("babad"))
print(Solution().longestPalindrome("ccc"))
print(Solution().longestPalindrome("bb"))
