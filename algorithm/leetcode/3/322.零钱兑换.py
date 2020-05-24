# -*- coding: utf-8 -*-
# 给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。
# 示例 1:
# 输入: coins = [1, 2, 5], amount = 11
# 输出: 3
# 解释: 11 = 5 + 5 + 1
# 示例 2:
# 输入: coins = [2], amount = 3
# 输出: -1
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/coin-change
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        cache = dict()

        def dp_opt(total, _amount):
            if _amount == 0:
                return total
            if (total, _amount) in cache:
                return cache[(total, _amount)]
            res = min(dp_opt(total + 1, _amount - coin) if _amount >= coin else float('inf') for coin in coins)
            cache[(total, _amount)] = res
            return res

        res = dp_opt(0, amount)
        print(cache)
        return res if res != float('inf') else -1


s = Solution()
res = s.coinChange([3, 7, 405, 436], 8839)
print(res)
