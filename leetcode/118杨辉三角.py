class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows ==0:
            return []
        result = [[1], [1, 1]]
        if numRows <= 2:
            return result[:numRows]
        for i in range(2, numRows):
            tmp = [1]
            for j in range(1, i + 1):
                if j == i:
                    tmp.append(1)
                else:
                    tmp.append(result[i - 1][j - 1] + result[i - 1][j])
            result.append(tmp)
        return result


if __name__ == '__main__':
    s = Solution()
    result = s.generate(5)
    print(result)
