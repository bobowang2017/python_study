# -*- coding: utf-8 -*-
# 给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
# 说明：每次只能向下或者向右移动一步。
# 示例:
# 输入:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# 输出: 7
# 解释: 因为路径 1→3→1→1→1 的总和最小。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/minimum-path-sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution(object):
    def minPathSum(self, grid):
        # 此数组用于记忆化搜索
        dp = [[0] * len(grid[0]) for i in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # 在起点的时候
                if i == 0 and j == 0:
                    dp[i][j] = grid[0][0]
                # 在左边缘的时候
                elif j == 0 and i != 0:
                    dp[i][j] = dp[i - 1][j] + grid[i][j]
                # 在上边缘的时候
                elif i == 0 and j != 0:
                    dp[i][j] = dp[i][j - 1] + grid[i][j]
                # 普遍情况下
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[len(grid) - 1][len(grid[0]) - 1]


s = Solution()
# res = s.minPathSum([
#     [1, 4, 5, 7],
#     [2, 4, 6, 8],
#     [2, 4, 8, 9],
#     [9, 5, 2, 1]
# ])

res = s.minPathSum([
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
])
# res = s.minPathSum([
#     [1, 4, 8, 6, 2, 2, 1, 7],
#     [4, 7, 3, 1, 4, 5, 5, 1],
#     [8, 8, 2, 1, 1, 8, 0, 1],
#     [8, 9, 2, 9, 8, 0, 8, 9],
#     [5, 7, 5, 7, 1, 8, 5, 5],
#     [7, 0, 9, 4, 5, 6, 5, 6],
#     [4, 9, 9, 7, 9, 1, 9, 0]
# ])


print(res)
