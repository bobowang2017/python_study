# -*- coding: utf-8 -*-
class SolutionOne(object):
    def __init__(self):
        self.data = []

    def rp(self, arr, n):
        if self.data[n] != -1:
            return self.data[n]
        if n == 0:
            return arr[0]
        if n == 1:
            return max(arr[0], arr[1])
        res = max(self.rp(arr, n - 1), self.rp(arr, n - 2) + arr[n])
        self.data[n] = res
        return res

    def massage(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        self.data = [-1 for i in range(len(nums))]
        res = self.rp(nums, len(nums) - 1)
        return res


s = SolutionOne()
print(s.massage([2, 1, 4, 5, 3, 1, 1, 3]))


class SolutionTwo(object):

    def massage(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 0:
            return 0
        if length == 1:
            return nums[0]
        data = [-1 for i in range(length)]
        data[0] = nums[0]
        data[1] = max(nums[0], nums[1])
        for i in range(2, length):
            data[i] = max(data[i-1], data[i-2] + nums[i])
        return data[length-1]


s = SolutionTwo()
print(s.massage([2, 1, 4, 5, 3, 1, 1, 3]))