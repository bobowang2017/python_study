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

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p1 = head
        # while p1:
        #     val = p1.val
        #     p2 = p1.next
        #     while p2:

