# -*- coding: utf-8 -*-
class Solution(object):

    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)

        cache = [[-1 for _ in range(length)] for _ in range(length)]

        def dp(i, j):
            if i > j:
                return 0
            if cache[i][j] != -1:
                return cache[i][j]
            if s[i] == s[j]:
                result = dp(i + 1, j - 1) + (1 if i == j else 2)

            else:
                result = max(
                    dp(i, j - 1),
                    dp(i + 1, j)
                )
            cache[i][j] = result
            return result

        if length == 1:
            return 1
        res = dp(0, length - 1)
        print(cache)
        return res


print(Solution().longestPalindromeSubseq("bbbab"))
print(Solution().longestPalindromeSubseq("cbbd"))
print(Solution().longestPalindromeSubseq("aaa"))
