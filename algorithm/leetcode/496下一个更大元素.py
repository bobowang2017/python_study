class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if not nums1 or not nums2:
            return []
        stack = list()
        stack.append(nums2[0])
        temp = dict()
        i, n = 1, len(nums2)
        while i < n:
            if stack[-1] < nums2[i]:
                while stack:
                    if stack[-1] >= nums2[i]:
                        break
                    temp[stack.pop()] = nums2[i]
                stack.append(nums2[i])
            else:
                stack.append(nums2[i])
            i += 1
        for s in stack:
            temp[s] = -1
        return [temp[num] for num in nums1]


if __name__ == '__main__':
    s = Solution()
    head = s.nextGreaterElement([2,4], [1,2,3,4])
    print(head)
