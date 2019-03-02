# 给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。
#
# 示例 1:
#
# 输入: 1->2->3->3->4->4->5
# 输出: 1->2->5
# 示例 2:
#
# 输入: 1->1->1->2->3
# 输出: 2->3


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        p = temp_head = ListNode(-1)
        temp_head.next = head
        while p.next:
            p1 = p2 = p.next
            while p2.next and p2.next.val == p1.val:
                p2 = p2.next
            if p1 == p2:
                p = p.next
            else:
                p.next = p2.next
        return temp_head.next
