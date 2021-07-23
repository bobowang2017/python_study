# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def new_list(self, array):
        root = ListNode(array[0])
        p = root
        for a in array[1:]:
            node = ListNode(a)
            p.next = node
            p = p.next
        return root

    def display(self, l):
        while l:
            print(l.val)
            l = l.next


    def mergeInBetween(self, list1, a, b, list2):
        """
        :type list1: ListNode
        :type a: int
        :type b: int
        :type list2: ListNode
        :rtype: ListNode
        """
        h1 = list1
        h2 = list2
        start = None
        end = None
        cnt = 0
        while h1:
            if cnt == a -1:
                start = h1
            if cnt == b + 1:
                end = h1
            h1 = h1.next
            cnt += 1
        tail = None
        while h2:
            tail = h2
            h2 = h2.next
        start.next = list2
        tail.next = end
        return list1


s = Solution()
list1 = s.new_list([0,1,2,3,4,5])
list2 = s.new_list([1000000,1000001,1000002])
s.display(list1)
s.display(list2)
result = s.mergeInBetween(list1, 3, 4, list2)
s.display(result)
