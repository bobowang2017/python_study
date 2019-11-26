# -*- coding: utf-8 -*-
# 根据每日 气温 列表，请重新生成一个列表，对应位置的输入是你需要再等待多久温度才会升高超过该日的天数。如果之后都不会升
# 高，请在该位置用 0 来代替。 例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 
# [1, 1, 4, 2, 1, 1, 0, 0]。
#
# 提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/daily-temperatures


class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        res = []
        stack = []
        length = len(T)
        _max = T[-1]
        for i in range(length - 1, -1, -1):
            if T[i] > _max:
                _max = T[i]
            if not stack:
                stack.append((i, T[i]))
                res.insert(0, 0)
            elif stack[-1][1] > T[i]:
                stack.append((i, T[i]))
                res.insert(0, 1)
            else:
                if T[i] > _max:
                    res.insert(0, 0)
                else:
                    tag = False
                    while stack:
                        if stack[-1][1] > T[i]:
                            res.insert(0, stack[-1][0] - i)
                            tag = True
                            break
                        else:
                            stack.pop()
                    if not tag:
                        res.insert(0, 0)
                    stack.append((i, T[i]))
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.dailyTemperatures([89, 62, 70, 58, 47, 47, 46, 76, 100, 70]))
