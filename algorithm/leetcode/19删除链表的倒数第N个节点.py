# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
# 示例：
# 给定一个链表: 1->2->3->4->5, 和 n = 2.
# 当删除了倒数第二个节点后，链表变为 1->2->3->5.
# 说明：
# 给定的 n 保证是有效的。
# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # 如果链表为空或者只有一个节点，则直接返回空，因为n>=1
        if not head or not head.next:
            return None
        p1 = p2 = head
        i = 0
        while i < n:
            p2 = p2.next
            i += 1
        # 如果刚好p2为空，则说明倒数第n个节点为头结点
        if not p2:
            return p1.next
        while p2.next:
            p1 = p1.next
            p2 = p2.next
        p1.next = p1.next.next
        return head
