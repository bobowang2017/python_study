class Solution(object):
    def threeSumClosest(self, nums, target):
        nums = sorted(nums)
        close = 100000
        result = 10000
        idx, length = 0, len(nums)
        while idx < length:
            t = target - nums[idx]
            i, j = idx + 1, length - 1
            while i < j:
                if nums[i] + nums[j] < t:
                    if t - (nums[i] + nums[j]) < close:
                        close = t - (nums[i] + nums[j])
                        result = nums[i] + nums[j] + nums[idx]
                    i += 1
                elif nums[i] + nums[j] > t:
                    if (nums[i] + nums[j]) - t < close:
                        close = (nums[i] + nums[j]) - t
                        result = nums[i] + nums[j] + nums[idx]
                    j -= 1
                else:
                    result = nums[i] + nums[j] + nums[idx]
                    break
            idx += 1
        return result


if __name__ == '__main__':
    solution = Solution()
    result = solution.threeSumClosest([0, 1, 2], 3)
    print(result)
