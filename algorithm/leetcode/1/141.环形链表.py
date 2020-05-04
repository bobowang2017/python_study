# -*- coding: utf-8 -*-
# 给定一个链表，判断链表中是否有环。
#
# 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/linked-list-cycle
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 算法思想：定义两个指针p, q，其中p每次向前移动一步，q每次向前移动两步，所以就成p为慢指针，q为快指针。
# 那么如果单链表存在环，则p和q进入环后一定会在某一点相遇，因为进入环后就会一直循环下去，否则q将首先遇到null，
# 就说明不存在环。

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        p = q = head
        while q.next and q.next.next:
            p = p.next
            q = q.next.next
            if p == q:
                return True
        return False

