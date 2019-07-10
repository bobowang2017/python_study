# 中位数，就是数组排序后处于数组最中间的那个元素。说来有些麻烦，如果数组长度是奇数，最中间就是位置为（n+1）／2的那个元素
# 。如果是偶数呢，标准的定义是位置为n/2和位置为n/2+1的两个元素的和除以2的结果，有些复杂。为了解答的方便，我们假设数组长
# 度暂且都为奇数吧。


class Solution(object):
    def maxSubArray(self, nums):
        # 初始小顶堆的建立

        pass

if __name__ == '__main__':
    s = Solution()
    data = s.maxSubArray([-4, -1, -2, 1])
    print(data)
