# -*- coding: utf-8 -*-
# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
# 问总共有多少条不同的路径？
# 示例 1:
# 输入: m = 3, n = 2
# 输出: 3
# 解释:
# 从左上角开始，总共有 3 条路径可以到达右下角。
# 1. 向右 -> 向右 -> 向下
# 2. 向右 -> 向下 -> 向右
# 3. 向下 -> 向右 -> 向右
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/unique-paths
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        data = dict()

        def opt(i, j):
            if i == 1 and j == 1:
                return 1
            if (i, j) in data:
                return data[(i, j)]
            _res = 0
            if i > 0:
                _res += opt(i - 1, j)
            if j > 0:
                _res += opt(i, j - 1)
            data[(i, j)] = _res
            return _res

        return opt(m, n)


s = Solution()
res = s.uniquePaths(3, 2)
print(res)