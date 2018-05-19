# 给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。
# 注意：
# 答案中不可以包含重复的四元组。
# 示例：
# 给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。
# 满足要求的四元组集合为：
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        for x in range(len(nums) - 3):
            for y in range(x + 1, len(nums) - 2):
                for z in range(y + 1, len(nums) - 1):
                    for h in range(z + 1, len(nums)):
                        if nums[x] + nums[y] + nums[z] + nums[h] == target:
                            data = []
                            data.append(nums[x])
                            data.append(nums[y])
                            data.append(nums[z])
                            data.append(nums[h])
                            result.append(data)
        temp = list()
        for m in result:
            if m not in temp:
                temp.append(m)
        return temp


solution = Solution()
result = solution.fourSum(
        [-498, -492, -473, -455, -441, -412, -390, -378, -365, -359, -358, -326, -311, -305, -277, -265, -264, -256,
         -254, -240, -237, -234, -222, -211, -203, -201, -187, -172, -164, -134, -131, -91, -84, -55, -54, -52, -50,
         -27, -23, -4, 0, 4, 20, 39, 45, 53, 53, 55, 60, 82, 88, 89, 89, 98, 101, 111, 134, 136, 209, 214, 220, 221,
         224, 254, 281, 288, 289, 301, 304, 308, 318, 321, 342, 348, 354, 360, 383, 388, 410, 423, 442, 455, 457, 471,
         488, 488]
        , -2808)
print(result)

a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)
