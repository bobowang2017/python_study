class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        data = str.strip()
        if not data:
            return 0
        result = []
        tag = False if data[0] == '-' else True
        data = data[1:] if not tag or data[0] == '+' else data
        if data.__len__() == 0:
            return 0
        for index, element in enumerate(data):
            if index == 0:
                if ord(element) < 48 or ord(element) > 57:
                    return 0
            if 48 <= ord(element) <= 57:
                result.append(element)
            else:
                break
        res = int("".join(result))
        res = res if tag else -res
        if res < -pow(2, 31):
            res = -pow(2, 31)
        if res > pow(2, 31) - 1:
            res = pow(2, 31) - 1
        return res


if __name__ == '__main__':
    solution = Solution()
    result = solution.myAtoi("  -0012a42")
    print(result)
