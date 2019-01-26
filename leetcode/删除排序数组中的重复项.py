# -*- coding: utf-8 -*-
# 给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。
#
# 不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
#
# 示例 1:
#
# 给定 nums = [1,1,1,2,2,3],
#
# 函数应返回新长度 length = 5, 并且原数组的前五个元素被修改为 1, 1, 2, 2, 3 。
#
# 你不需要考虑数组中超出新长度后面的元素。
# 示例 2:
#
# 给定 nums = [0,0,1,1,1,1,2,3,3],
#
# 函数应返回新长度 length = 7, 并且原数组的前五个元素被修改为 0, 0, 1, 1, 2, 3, 3 。
#
# 你不需要考虑数组中超出新长度后面的元素。

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        counter = 0
        sum = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                counter += 1
            else:
                if counter >= 2:
                    sum += (counter - 1)
                counter = 0
            i += 1
        return len(nums) - sum


if __name__ == '__main__':
    s = Solution()
    data = s.removeDuplicates([1,1,1,2,2,3])
    print(data)
