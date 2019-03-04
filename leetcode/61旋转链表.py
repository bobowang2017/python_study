# 给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。
# 示例 1:
# 输入: 1->2->3->4->5->NULL, k = 2
# 输出: 4->5->1->2->3->NULL
# 解释:
# 向右旋转 1 步: 5->1->2->3->4->NULL
# 向右旋转 2 步: 4->5->1->2->3->NULL
# 示例 2:
# 输入: 0->1->2->NULL, k = 4
# 输出: 2->0->1->NULL
# 解释:
# 向右旋转 1 步: 2->0->1->NULL
# 向右旋转 2 步: 1->2->0->NULL
# 向右旋转 3 步: 0->1->2->NULL
# 向右旋转 4 步: 2->0->1->NULL


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def linklist_init(data):
    if not isinstance(data, list) or len(data) == 0:
        raise Exception('Params Error')
    head = ListNode(data[0])
    tail = head
    for d in data[1:]:
        node = ListNode(d)
        tail.next = node
        tail = tail.next
    return head


def display(head):
    if not isinstance(head, ListNode):
        raise Exception('Params Error')
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return []
        p = head
        length = 1
        while p.next:
            length += 1
            p = p.next
        if length == 1:
            return head
        real_k = k % length
        p.next = head
        i = 1
        p1, p2 = head, head.next
        while i < length - real_k:
            p2 = p2.next
            p1 = p1.next
            i += 1
        head = p2
        p1.next = None
        return head


if __name__ == '__main__':
    head = linklist_init([1, 2])
    display(head)
    s = Solution()
    result = s.rotateRight(head, 1)
    display(result)
