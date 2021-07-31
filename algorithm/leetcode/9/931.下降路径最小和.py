# -*- coding: utf-8 -*-
class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        length = len(matrix)
        op = [[-1 for _ in range(length)] for _ in range(length)]
        op[0] = matrix[0]
        for i in range(1, length):
            for j in range(length):
                if j - 1 >= 0 and j + 1 < length:
                    op[i][j] = min(op[i - 1][j - 1] + matrix[i][j], op[i - 1][j] + matrix[i][j],
                                   op[i - 1][j + 1] + matrix[i][j])
                elif j - 1 < 0:
                    op[i][j] = min(op[i - 1][j] + matrix[i][j], op[i - 1][j + 1] + matrix[i][j])
                else:
                    op[i][j] = min(op[i - 1][j] + matrix[i][j], op[i - 1][j - 1] + matrix[i][j])
        return min(op[length - 1])


print(Solution().minFallingPathSum([[2, 1, 3], [6, 5, 4], [7, 8, 9]]))
print(Solution().minFallingPathSum([[-19, 57], [-40, -5]]))
