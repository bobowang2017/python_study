# -*- coding: utf-8 -*-
# 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。


class Solution(object):
    def multiply(self, num1, num2):
        if num1 == '0' or num2 == '0':
            return 0
        data1 = list(num1)
        data2 = list(num2)
        result = [[-1] * len(data1) for i in range(len(data2))]
        print(result)
        for x in range(len(data2) - 1, -1, -1):
            for y in range(len(data1) - 1, -1, -1):
                result[x][y] = int(data2[x]) * int(data1[y])
        print(result)
        data = [0] * (max(len(data1), len(data2)) + 1)
        k = len(data) - 1
        temp = 0
        for x in range(len(data1) - 1, -1, -1):
            total = 0
            for y in range(len(data2) - 1, -1, -1):
                total += result[y][x]
            temp = temp / 10
            total += temp
            data[k] = total % 10
            k -= 1
        print(data)
        return 0


if __name__ == '__main__':
    s = Solution()
    data = s.multiply('123', '456')
    print(data)
