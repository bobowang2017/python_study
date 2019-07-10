# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
# 示例：
#
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def linklist_init(self, data):
        head = ListNode(data[0])
        tail = head
        for d in data[1:]:
            node = ListNode(d)
            tail.next = node
            tail = tail.next
        return head

    def display(self, head):
        if not isinstance(head, ListNode):
            raise Exception('Params Error')
        res = []
        while head:
            res.append(head.val)
            head = head.next
        print(res)

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1, p2 = l1, l2
        result = ListNode(-1)
        p3 = result
        temp = 0
        while p1 and p2:
            val = p1.val + p2.val + temp if p1.val + p2.val + temp < 10 else (p1.val + p2.val + temp) % 10
            temp = 0 if p1.val + p2.val + temp < 10 else 1
            p3.next = ListNode(val)
            p3 = p3.next
            p1 = p1.next
            p2 = p2.next
        if p1:
            while p1:
                val = p1.val + temp if p1.val + temp < 10 else (p1.val + temp) % 10
                temp = 0 if p1.val + temp < 10 else 1
                p3.next = ListNode(val)
                p3 = p3.next
                p1 = p1.next
        if p2:
            while p2:
                val = p2.val + temp if p2.val + temp < 10 else (p2.val + temp) % 10
                temp = 0 if p2.val + temp < 10 else 1
                p3.next = ListNode(val)
                p3 = p3.next
                p2 = p2.next
        if temp == 1:
            p3.next = ListNode(1)
        return result.next


if __name__ == '__main__':
    s = Solution()
    s1 = s.linklist_init([5, 4, 3, 4, 4, 5])
    s2 = s.linklist_init([5, 5, 6])
    result = s.addTwoNumbers(s1, s2)
    s.display(result)
