class Solution:
    def checkPerfectNumber(self, num):
        ans = 1
        if num % 2 != 0:
            return False
        for i in range(1, num):
            if num % (2 ** i) == 0:
                ans += 2 ** i
                if ans == num / (2 ** i):
                    return True
            if num < 2 ** i:
                return False
        return False


s = Solution()
result = s.checkPerfectNumber(28)
print(result)