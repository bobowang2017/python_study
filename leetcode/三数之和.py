# 给定一个包含n个整数的数组nums，判断nums中是否存在三个元素a，b，c ，使得a + b + c = 0 ？找出所有满足条件且不重复的三元组。
# 注意：答案中不可以包含重复的三元组。
#
# 例如, 给定数组
# nums = [-1, 0, 1, 2, -1, -4]，
#
# 满足要求的三元组集合为：
# [
#     [-1, 0, 1],
#     [-1, -1, 2]
# ]
# 分析：本题算法比较简单，主要考点是算法的时间复杂度


class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = 0 - nums[i]
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[j] + nums[k] == target:
                    res.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif nums[j] + nums[k] < target:
                    j += 1
                else:
                    k -= 1
        return res


if __name__ == '__main__':
    solution = Solution()
    result = solution.threeSum([-1, 0, 1, 2, -1, -4])
    print(result)
