# -*- coding: utf-8 -*-


class Solution:
    def findTargetSumWays(self, nums, target):
        result = {}
        def back(sum, i):
            if (sum, i) in result:
                return result[(sum, i)]
            if i == len(nums) and sum == target:
                return 1
            elif i == len(nums):
                return 0
            A = back(sum + nums[i], i + 1)
            B = back(sum - nums[i], i + 1)
            result[(sum + nums[i], i + 1)] = A
            result[(sum - nums[i], i + 1)] = B
            return A + B
        return back(0, 0)


print(Solution().findTargetSumWays([1, 1, 1, 1, 1], 3))
