# 给定一个按非递减顺序排序的整数数组
# A，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。
# 示例1：
# 输入：[-4, -1, 0, 3, 10]
# 输出：[0, 1, 9, 16, 100]
# 示例2：
# 输入：[-7, -3, 2, 3, 11]
# 输出：[4, 9, 9, 49, 121]


class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        result = []
        i, j = 0, len(A) - 1
        while i < j:
            a, b = abs(A[i]), abs(A[j])
            if a > b:
                result.append(pow(a, 2))
                i += 1
            elif a == b:
                result.append(pow(a, 2))
                result.append(pow(b, 2))
                i += 1
                j -= 1
            else:
                result.append(pow(b, 2))
                j -= 1
        if i == j:
            result.append(pow(A[i], 2))
        return sorted(result, reverse=True)


if __name__ == '__main__':
    solution = Solution()
    result = solution.sortedSquares([-4, -1, 0, 3, 10])
    print(result)
