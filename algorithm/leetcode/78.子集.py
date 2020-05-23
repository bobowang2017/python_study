# -*- coding: utf-8 -*-
# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
# 说明：解集不能包含重复的子集。
# 示例:
# 输入: nums = [1,2,3]
# 输出:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/subsets
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []

        def rec_display(i, res):
            if i > len(nums) - 1:
                result.append(res)
                return
            rec_display(i + 1, res + [nums[i]])
            rec_display(i + 1, res)

        rec_display(0, [])
        return result


s = Solution()
res = s.subsets(nums=[1, 2, 3])
print(res)
