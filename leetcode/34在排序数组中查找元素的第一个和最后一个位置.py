# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
# 你的算法时间复杂度必须是 O(log n) 级别。
# 如果数组中不存在目标值，返回 [-1, -1]。
# 示例 1:
# 输入: nums = [5,7,7,8,8,10], target = 8
# 输出: [3,4]
# 示例 2:
# 输入: nums = [5,7,7,8,8,10], target = 6
# 输出: [-1,-1]


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start, end = 0, len(nums) - 1
        temp = -1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                temp = mid
                break
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        if temp == -1:
            return [-1, -1]
        i = j = temp
        while i >= 0:
            if nums[i] == target:
                i -= 1
            else:
                break
        while j < len(nums):
            if nums[j] == target:
                j += 1
            else:
                break
        return [i + 1, j - 1]


if __name__ == '__main__':
    s = Solution()
    s1 = s.searchRange([5, 7, 7, 8, 8, 10], 6)
    print(s1)
