# 给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。
# 示例 :
# 输入: [1,2,1,3,2,5]
# 输出: [3,5]
# 注意：
# 结果输出的顺序并不重要，对于上面的例子， [5, 3] 也是正确答案。
# 你的算法应该具有线性时间复杂度。你能否仅使用常数空间复杂度来实现？
from functools import reduce


class Solution(object):
    def reduce(self, nums):
        i, result = 1, nums[0]
        while i < len(nums):
            result ^= nums[i]
            i += 1
        return result

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = self.reduce(nums)
        temp = '{:08b}'.format(result)
        for index, s in enumerate(temp):
            if s == '1':
                break
        bin_data = ['{:08b}'.format(num) for num in nums]
        result1 = [int(data, 2) for data in bin_data if data[index] == '0']
        result2 = [int(data, 2) for data in bin_data if data[index] == '1']
        return [self.reduce(result1), self.reduce(result2)]


if __name__ == '__main__':
    s = Solution()
    result = s.singleNumber([1, 2, 1, 3, 2, 5])
    print(result)
