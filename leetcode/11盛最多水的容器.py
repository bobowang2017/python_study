# 给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为
# (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
# 说明：你不能倾斜容器，且 n 的值至少为 2。


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start, end = 0, len(height)-1
        max_area = 0
        while start < end:
            h1, h2 = height[start], height[end]
            area = min(h1, h2) * (end - start)
            if max_area < area:
                max_area = area
            if h1 < h2:
                start += 1
            else:
                end -= 1
        return max_area


if __name__ == '__main__':
    s = Solution()
    data = s.maxArea([1,8,6,2,5,4,8,3,7])
    print(data)
