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
        if not isinstance(head, ListNode):
            raise Exception('Params Error')
        res = []
        while head:
            res.append(head.val)
            head = head.next
        print(res)

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if n <= 0:
            return head
        p1 = p2 = head
        for i in range(n):
            p1 = p1.next
        while p1.next:
            p1 = p1.next
            p2 = p2.next
        p2.next = p2.next.next
        return head


if __name__ == '__main__':
    solution = Solution()
    head = solution.linklist_init([1])
    solution.display(head)
    solution.removeNthFromEnd(head, 1)
    solution.display(head)
