class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == 0 or num2 == 0:
            return "0"
        l1, l2 = len(num1), len(num2)
        ans = [0] * (l1 + l2)
        for i in range(l1)[::-1]:
            for j in range(l2)[::-1]:
                ans[i + j] += int(num1[i]) * int(num2[j])
        sum = 0
        for i in range(len(ans))[::-1]:
            temp = ans[i] + sum
            ans[i] = str(temp % 10)
            sum = temp // 10
        if sum != 0:
            ans.insert(0, str(sum))
        return "".join(ans[:len(ans) - 1])


if __name__ == '__main__':
    s = Solution()
    result = s.multiply("91033", "0")
    print(result)
