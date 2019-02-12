# -*- coding: utf-8 -*-
# 给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
#
# 不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。


class Solution(object):
    def removeDuplicates(self, nums):
        i = 0
        tag = 1
        counter = 0
        while i < len(nums) - 1 and tag < len(nums):
            if nums[i] == nums[tag]:
                tag += 1
                counter += 1
                continue
            else:
                nums[i + 1] = nums[tag]
                i += 1
                tag += 1
        print(nums[:len(nums) - counter])
        return len(nums[:len(nums) - counter])


if __name__ == '__main__':
    s = Solution()
    data = s.removeDuplicates([1, 1, 2])
    print(data)
