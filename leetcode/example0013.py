# -*- coding: utf-8 -*-
# 给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
#
# 不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。


class Solution(object):
    def removeDuplicates(self, nums):
        total = 0
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                total += 1
            i += 1
        return len(nums) - total


if __name__ == '__main__':
    s = Solution()
    data = s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
    print(data)
