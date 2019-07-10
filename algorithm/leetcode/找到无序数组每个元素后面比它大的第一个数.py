# n个整数的无序数组，找到每个元素后面比它大的第一个数，要求时间复杂度为O(N)，在面试官提醒下写出来了，用栈+栈底指针
class Solution(object):
    def find(self, nums):
        stack = [nums[0]]
        result = dict()
        i = 1
        while i < len(nums):
            while len(stack) > 0 and stack[-1] < nums[i]:
                result[stack.pop()] = nums[i]
            stack.append(nums[i])
            i += 1
        return result


if __name__ == '__main__':
    s = Solution()
    data = s.find([7, 6, 5, 4, 3, 2, 1, 10])
    print(data)
