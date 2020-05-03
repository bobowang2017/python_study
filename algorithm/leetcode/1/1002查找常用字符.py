# 给定仅有小写字母组成的字符串数组
# A，返回列表中的每个字符串中都显示的全部字符（包括重复字符）组成的列表。例如，如果一个字符在每个字符串中出现3次，但不是
# 4次，则需要在最终答案中包含该字符3次。你可以按任意顺序返回答案。
# 示例1：
# 输入：["bella", "label", "roller"]
# 输出：["e", "l", "l"]
# 示例2：
# 输入：["cool", "lock", "cook"]
# 输出：["c", "o"]


class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        result = []
        tmp_list = []
        for a in A:
            tmp = [0] * 26
            for aa in a:
                tmp[ord(aa) - ord('a')] += 1
            tmp_list.append(tmp)
        l = len(tmp_list)
        for j in range(0, 26):
            min = 65535
            for i in range(l):
                if tmp_list[i][j] < min:
                    min = tmp_list[i][j]
            for k in range(min):
                result.append(chr(ord('a') + j))
        return result


if __name__ == '__main__':
    s = Solution()
    result = s.commonChars(["bella","label","roller"])
    print(result)
