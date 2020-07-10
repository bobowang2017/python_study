# -*- coding: utf-8 -*-
# 在给定的网格中，每个单元格可以有以下三个值之一：
#
# 值 0 代表空单元格；
# 值 1 代表新鲜橘子；
# 值 2 代表腐烂的橘子。
# 每分钟，任何与腐烂的橘子（在 4 个正方向上）相邻的新鲜橘子都会腐烂。
#
# 返回直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/rotting-oranges
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution(object):
    def rot(self, grid, m, n, i, j):
        tag = False
        if i - 1 >= 0 and grid[i - 1][j] == 1:
            tag = True
            grid[i - 1][j] = 2
        if i + 1 < m and grid[i + 1][j] == 1:
            grid[i + 1][j] = 2
            tag = True
        if j - 1 >= 0 and grid[i][j - 1] == 1:
            grid[i][j - 1] = 2
            tag = True
        if j + 1 < n and grid[i][j + 1] == 1:
            grid[i][j + 1] = 2
            tag = True
        return tag

    def log(self, grid):
        print('=' * 60)
        for g in grid:
            print(g)
        print('=' * 60)

    def check_rot(self, grid, m, n):
        tag = False
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    tag = True
                    break
        return tag

    def bfs(self, grid, m, n):
        counter = 0
        while True:
            find_tag = False
            # self.log(grid)
            rot_point = []
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 2:
                        rot_point.append((i, j))
            for r in rot_point:
                res = self.rot(grid, m, n, r[0], r[1])
                if not find_tag:
                    find_tag = res
            if not find_tag:
                break
            counter += 1
        if self.check_rot(grid, m, n):
            return -1
        return counter

    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        return self.bfs(grid, m, n)


class Solution2(object):
    def orangesRotting(self, grid) -> int:
        x, y, time = len(grid), len(grid[0]), 0
        D, queue = [[-1, 0], [0, -1], [0, 1], [1, 0]], []  # 四个方向的坐标和队列
        for i in range(x):
            for j in range(y):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
        while queue:
            i, j, time = queue.pop(0)
            for d in D:
                loc_i, loc_j = i + d[0], j + d[1]
                if 0 <= loc_i < x and 0 <= loc_j < y and grid[loc_i][loc_j] == 1:
                    grid[loc_i][loc_j] = 2
                    queue.append((loc_i, loc_j, time + 1))
        for g in grid:
            if 1 in g:
                return -1
        return time
