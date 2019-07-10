# 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
# 示例 1:
# 输入: [1,2,3,4,5,6,7] 和 k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右旋转 1 步: [7,1,2,3,4,5,6]
# 向右旋转 2 步: [6,7,1,2,3,4,5]
# 向右旋转 3 步: [5,6,7,1,2,3,4]
# 示例 2:
# 输入: [-1,-100,3,99] 和 k = 2
# 输出: [3,99,-1,-100]
# 解释:
# 向右旋转 1 步: [99,-1,-100,3]
# 向右旋转 2 步: [3,99,-1,-100]


class Solution:
    def reverse(self, nums, start, end):
        i = start
        j = end
        while i < j:
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
            i += 1
            j -= 1

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        k %= l
        self.reverse(nums, 0, l - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, l - 1)
        print(nums)


if __name__ == '__main__':
    s = Solution()
    result = s.rotate([1, 2, 3, 4, 5, 6, 7], 3)
    print(result)
