# 给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def display(self, head):
        res = []
        while head:
            res.append(head.val)
            head = head.next
        print(res)

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

    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        total = set()
        total.add(head.val)
        p1, p2 = head, head.next
        while p2:
            if p2.val not in total:
                total.add(p2.val)
            else:
                p1.next = p2.next
                p2 = p1.next
                continue
            p1 = p1.next
        return head


if __name__ == '__main__':
    s = Solution()
    head = s.linklist_init([])
    s.display(head)
    result = s.deleteDuplicates(head)
    s.display(result)
