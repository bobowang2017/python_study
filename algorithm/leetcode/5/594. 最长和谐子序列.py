# -*- coding: utf-8 -*-
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        data = {}
        for num in nums:
            if num in data:
                data[num] += 1
            else:
                data[num] = 1
        new_list = sorted(data.keys())
        if len(new_list) == 1:
            return 0
        result = 0
        idx = 0
        while idx < len(new_list):
            if new_list[idx] + 1 in data:
                tmp = data[new_list[idx]] + data[new_list[idx] + 1]
                if tmp > result:
                    result = tmp
            idx += 1
        return 0 if result == 1 else result


# 需要注意的是如果列表元素只包含相同元素、或者相同元素的最大值是不计算入内的

print(Solution().findLHS([1, 3, 5, 7, 9, 11, 13, 15, 17]))
print(Solution().findLHS([1, 3, 2, 2, 5, 2, 3, 7]))
print(Solution().findLHS([1, 2, 3, 4]))
print(Solution().findLHS([1, 1, 1, 1]))
print(Solution().findLHS([1, 2, 2, 1]))
print(Solution().findLHS([1, 4, 1, 3, 1, -14, 1, -13]))
