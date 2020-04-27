# -*- coding: utf-8 -*-
# 给定一个单链表，随机选择链表的一个节点，并返回相应的节点值。保证每个节点被选的概率一样。
#
# 进阶:
# 如果链表十分大且长度未知，如何解决这个问题？你能否使用常数级空间复杂度实现？
#
# 示例:
#
# // 初始化一个单链表 [1,2,3].
# ListNode head = new ListNode(1);
# head.next = new ListNode(2);
# head.next.next = new ListNode(3);
# Solution solution = new Solution(head);
#
# // getRandom()方法应随机返回1,2,3中的一个，保证每个元素被返回的概率相等。
# solution.getRandom();

# 思想：遍历链表的时候，每到一个节点就生成一个随机数，遍历结束的时候，取随机数最大的那个节点即可。
import random


class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        p = self.head
        max, val = -1, 0
        while p:
            _r = random.randint()
            if _r > max:
                max, val = _r, p.val
            p = p.next
        return val
