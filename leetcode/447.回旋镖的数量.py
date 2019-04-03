import collections


class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        def distance(p1, p2):
            return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

        num = len(points)
        if num < 3:
            return 0
        count = 0
        dists = [[0] * num for _ in range(num)]  # 用[[0]*num]*num 会N行一起跟着变，因为list*n是浅拷贝
        for i in range(num - 1):
            for j in range(i, num):
                dists[j][i] = dists[i][j] = distance(points[i], points[j])  # 对称矩阵
        for r in dists:
            cc = collections.Counter(r)
            for k, v in cc.items():
                if v > 1:
                    count += v * (v - 1)  # 具有公共点的n条边中，任选两条来组成回旋镖，后两个点可以交换顺序，2*Cn2 = n*(n-1)
        return count


if __name__ == '__main__':
    s = Solution()
    result = s.numberOfBoomerangs([[0, 0], [1, 0], [2, 0]])
    print(result)
