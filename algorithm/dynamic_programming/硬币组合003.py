# -*- coding: utf-8 -*-
# 有面值分别为1，3，5的三种硬币若干，需要凑成11元最少需要多少硬币，凑成n元最少需要多少硬币？


def res_opt(n):
    # 自底向上
    # dp[i] 表示金额为i需要最少的硬币
    # dp[i] = min(dp[i], dp[i - coins[j]]) j所有硬币

    dp = [float("inf")] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        dp[i] = min(dp[i - c] if i - c >= 0 else float("inf") for c in [1, 3, 5]) + 1
    return dp[-1] if dp[-1] != float("inf") else -1


res = res_opt(100)
print(res)
