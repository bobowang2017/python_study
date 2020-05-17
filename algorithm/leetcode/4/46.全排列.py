# -*- coding: utf-8 -*-
# 给定一个 没有重复 数字的序列，返回其所有可能的全排列。
#
# 示例:
#
# 输入: [1,2,3]
# 输出:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/permutations
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
import copy


class Solution(object):
    def __init__(self):
        self.nums = None
        self.result = []

    def swap(self, i, j, nums):
        nums[i], nums[j] = nums[j], nums[i]

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.nums = nums
        length = len(nums)
        temp_num = copy.deepcopy(self.nums)
        for i in range(0, length):
            self.swap(0, i, temp_num)
            self.display(temp_num, 1)
        return self.result

    def display(self, temp_num, idx):
        if idx >= len(self.nums):
            self.result.append(temp_num)
        temp_num = copy.deepcopy(temp_num)
        for i in range(idx, len(self.nums)):
            self.swap(idx, i, temp_num)
            self.display(temp_num, idx+1)


s = Solution()
res = s.permute([1,2,3,4])
print(res)
