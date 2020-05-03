class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt, ret = 0, 0
        for num in nums:
            if cnt == 0:
                ret = num
            if num != ret:
                cnt -= 1
            else:
                cnt += 1
        return ret


if __name__ == '__main__':
    s = Solution()
    result = s.majorityElement([2, 2, 1, 3, 4, 5, 6, 2])
    print(result)