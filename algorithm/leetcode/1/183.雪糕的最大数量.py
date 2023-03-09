class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        n = len(costs)
        w = coins
        dp = [[0 for _ in range(w + 2)] for _ in range(n + 2)]
        for i in range(1, n + 1):
            for j in range(1, w + 1):
                if j >= costs[i - 1]:
                    dp[i][j] = max(dp[i - 1][j - costs[i - 1]] + 1, dp[i - 1][j])
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[n][w]


s = Solution()

print(s.maxIceCream([1,6,3,1,2,5], 20))
