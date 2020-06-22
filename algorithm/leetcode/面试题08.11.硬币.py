# -*- coding: utf-8 -*-
# 硬币。给定数量不限的硬币，币值为25分、10分、5分和1分，编写代码计算n分有几种表示法。
# (结果可能会很大，你需要将结果模上1000000007)
# 示例1:
#  输入: n = 5
#  输出：2
#  解释: 有两种方式可以凑成总金额:
# 5=5
# 5=1+1+1+1+1
# 示例2:
#  输入: n = 10
#  输出：4
#  解释: 有四种方式可以凑成总金额:
# 10=10
# 10=5+5
# 10=5+1+1+1+1+1
# 10=1+1+1+1+1+1+1+1+1+1
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/coin-lcci
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution(object):

    def __init__(self):
        self.temp_res = {}
        self.result = 0

    def res_opt(self, n):
        if n ==0:
            self.result += 1
            print('========')
            return
        print('-->{}'.format(n))
        if n >= 1:
            self.res_opt(n - 1)
        if n >= 5:
            self.res_opt(n - 5)
        if n >= 10:
            self.res_opt(n - 10)
        if n >= 25:
            self.res_opt(n - 25)

    def waysToChange(self, n):
        coins = [25, 10, 5, 1]
        # 注意dp的初始化，表示没有硬币情况下凑金额0-n分
        dp = [0] * (n + 1)
        dp[0] = 1  # 没有硬币凑0分为1种方式
        for i in range(len(coins)):
            for j in range(coins[i], n + 1):
                dp[j] += dp[j - coins[i]]
        return dp[-1] % 1000000007


print(Solution().waysToChange(10))
