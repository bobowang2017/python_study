# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def new_list(self, data):
        head = ListNode(data[0])
        p = head
        for idx, d in enumerate(data):
            if idx == 0:
                continue
            node = ListNode(d)
            p.next = node
            p = p.next
        return head

    def display(self, head):
        res = []
        while head:
            res.append(head.val)
            head = head.next
        print(res)

    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre_head = ListNode(-1)
        pre_head.next = head
        p = pre_head
        p1 = head
        while p1:
            p2 = p1.next
            if not p2:
                break
            p1.next = p2.next
            p2.next = p1
            pre_head.next = p2
            pre_head = p1
            p1 = p1.next
        return p.next


s = Solution()
head = s.new_list([1, 2, 3, 5, 6])
s.display(head)
res = s.swapPairs(head)
s.display(res)

head = s.new_list([1])
s.display(head)
res = s.swapPairs(head)
s.display(res)

head = s.new_list([1, 2])
s.display(head)
res = s.swapPairs(head)
s.display(res)
