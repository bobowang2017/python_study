class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        m = len(word1)
        n = len(word2)
        memo = [[-1 for _ in range(n)] for _ in range(m)]

        def dp(i, j):
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
            if memo[i][j] != -1:
                return memo[i][j]
            if word1[i] == word2[j]:
                memo[i][j] = dp(i + 1, j + 1)
            else:
                memo[i][j] = min(
                    dp(i + 1, j) + 1,
                    dp(i, j + 1) + 1
                )
            return memo[i][j]

        return dp(0, 0)


print(Solution().minDistance("sea", "eat"))
print(Solution().minDistance("abcd", "bcd"))
print(Solution().minDistance("abcde", "bd"))
