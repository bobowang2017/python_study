# 在无限的整数序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...中找到第 n 个数字。
# 注意:
# n 是正数且在32为整形范围内 ( n < 231)。
# 示例 1:
# 输入:3
# 输出:3
# 示例 2:
# 输入:11
# 输出:0
# 说明:第11个数字在序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... 里是0，它是10的一部分。


class Solution(object):
    def findNthDigit(self, n):
        i = count = 1
        while True:
            tmp = str(i)
            l = len(tmp)
            if count + l < n:
                count += l
            elif count <= n < count + l:
                j = 0
                while j < l:
                    count += 1
                    if count == n:
                        return str(i)[j + 1]
                    j += 1
            elif count + l == n:
                return str(i)[-1]
            i += 1


if __name__ == '__main__':
    s = Solution()
    result = s.findNthDigit(18)
    print(result)
