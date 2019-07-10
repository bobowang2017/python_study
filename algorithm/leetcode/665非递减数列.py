# 给定一个长度为 n 的整数数组，你的任务是判断在最多改变 1 个元素的情况下，该数组能否变成一个非递减数列。
# 我们是这样定义一个非递减数列的： 对于数组中所有的 i (1 <= i < n)，满足 array[i] <= array[i + 1]。
# 示例 1:
# 输入: [4,2,3]
# 输出: True
# 解释: 你可以通过把第一个4变成1来使得它成为一个非递减数列。
# 示例 2:
# 输入: [4,2,1]
# 输出: False
# 解释: 你不能在只改变一个元素的情况下将其变为非递减数列。

# 解题思路：
# 1、分别从左向右和从右向左找到第一个非有序的地方。
# 2、看看这两个非有序的索引相差的位置是不是小于等于1的并且前端的最右边head和后段的最左边next是不是也是有序的。如果都满足
# 的话就返回true。边界问题是用左边界设为整数的最小值Integer.MIN_VALUE，右边界设置为整数的最大值Integer.MAX_VALUE来解决的。


class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i, j = 0, len(nums) - 1
        while i < j and nums[i] <= nums[i + 1]:
            i += 1
        while i < j and nums[j] >= nums[j - 1]:
            j -= 1
        if i == 0:
            head = -65535
        else:
            head = nums[i - 1]
        next = 65535 if j == len(nums) - 1 else nums[j + 1]
        if j - i <= 1 and (head <= nums[j] or nums[i] <= next):
            return True
        else:
            return False


solution = Solution()
result = solution.checkPossibility([3, 4, 2, 3])
print(result)
