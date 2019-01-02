# -*- coding: utf-8 -*-
# 给定一个未排序的整数数组，找出其中没有出现的最小的正整数。
#
# 示例 1:
#
# 输入: [1,2,0]
# 输出: 3
# 示例 2:
#
# 输入: [3,4,-1,1]
# 输出: 2
# 示例 3:
#
# 输入: [7,8,9,11,12]
# 输出: 1


class Solution(object):
    def firstMissingPositive(self, nums):
        max = 0
        for num in nums:
            if num > max:
                max = num
        counter = [0] * (max + 1)
        result = None
        for data in nums:
            if data > 0:
                counter[data] += 1
        for index, data in enumerate(counter):
            if index != 0 and data == 0:
                result = index
                break
        if not result:
            result = max + 1
        return result


if __name__ == '__main__':
    s = Solution()
    data = s.firstMissingPositive([])
    print(data)
