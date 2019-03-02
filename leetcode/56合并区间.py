# 给出一个区间的集合，请合并所有重叠的区间。
# 示例 1:
# 输入: [[1,3],[2,6],[8,10],[15,18]]
# 输出: [[1,6],[8,10],[15,18]]
# 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
# 示例 2:
# 输入: [[1,4],[4,5]]
# 输出: [[1,5]]
# 解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。


class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals = sorted(intervals, key=lambda interval: interval.start)
        i = 1
        while i < len(intervals):
            if intervals[i].start > intervals[i - 1].end:
                i += 1
            elif intervals[i].start <= intervals[i - 1].end:
                new_area = Interval(intervals[i - 1].start, max(intervals[i - 1].end, intervals[i].end))
                intervals.pop(i - 1)
                intervals.pop(i - 1)
                intervals.insert(i - 1, new_area)
        return [[interval.start, interval.end] for interval in intervals]


if __name__ == '__main__':
    s = Solution()
    # data = [[1, 3], [2, 6], [15, 18], [8, 10]]
    data = [[1, 4], [4, 5]]
    result = s.merge([Interval(d[0], d[1]) for d in data])
    print(result)
