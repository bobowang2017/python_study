# -*- coding: utf-8 -*-
class cmp(str):
    def __lt__(self, other):
        return self + other < other + self


class Solution:
    def minNumber(self, nums: [int]) -> str:
        nums = sorted([str(i) for i in nums], key=cmp)
        return "".join(nums)


s = Solution()
print(s.minNumber([3,30,34,5,52,9,81]))