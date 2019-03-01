# 给定一个非负整数c ，你要判断是否存在两个整数a和b，使得a2 + b2 = c。
#
# 示例1:
# 输入: 5
# 输出: True
# 解释: 1 * 1 + 2 * 2 = 5
# 示例2:
# 输入: 3
# 输出: False
from math import sqrt, ceil


class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        a, b = 0, ceil(sqrt(c))
        while a <= b:
            if a * a + b * b == c:
                return True
            elif a * a + b * b < c:
                a += 1
            else:
                b -= 1
        return False


solution = Solution()
result = solution.judgeSquareSum(5)
print(result)
