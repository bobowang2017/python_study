# 给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。
# 请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，时间复杂度应为 O(nodes)，nodes 为节点总数。
# 示例 1:
# 输入: 1->2->3->4->5->NULL
# 输出: 1->3->5->2->4->NULL
# 示例 2:
# 输入: 2->1->3->5->6->4->7->NULL
# 输出: 2->3->6->7->1->5->4->NULL
# 说明:
# 应当保持奇数节点和偶数节点的相对顺序。
# 链表的第一个节点视为奇数节点，第二个节点视为偶数节点，以此类推。


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

    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        p1 = head1 = head
        p2 = head2 = head.next
        while p2:
            p1.next = p2.next
            if p2.next:
                p2.next = p2.next.next
            else:
                p2.next = None
            if p1.next:
                p1 = p1.next
            p2 = p2.next
        p1.next = head2
        return head1


if __name__ == '__main__':
    s = Solution()
    head = s.linklist_init([1, 2, 3, 4, 5, 6, 7, 8])
    s.display(head)
    s.oddEvenList(head)
    s.display(head)
