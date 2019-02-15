# -*- coding: utf-8 -*-
# 删除链表中等于给定值 val 的所有节点。
# 示例:
# 输入: 1->2->6->3->4->5->6, val = 6
# 输出: 1->2->3->4->5

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def linklist_init(self, data):
        if not isinstance(data, list) or len(data) == 0:
            raise Exception('Params Error')
        head = ListNode(data[0])
        tail = head
        for d in data[1:]:
            node = ListNode(d)
            tail.next = node
            tail = tail.next
        return head

    def display(self, head):
        res = []
        while head:
            res.append(head.val)
            head = head.next
        print(res)

    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode        """

        if not head:
            return
        while head:
            if head.val == val:
                head = head.next
            else:
                break
        if not head:
            return
        p1, p2 = head, head.next
        if p2:
            while p2.next:
                if p2.val == val:
                    p1.next = p2.next
                    p2 = p1.next
                else:
                    p1 = p2
                    p2 = p2.next
            if p2.val == val:
                p1.next = None
        return head


if __name__ == '__main__':
    s = Solution()
    head = s.linklist_init([1])
    s.display(head)
    result = s.removeElements(head, 1)
    s.display(result)