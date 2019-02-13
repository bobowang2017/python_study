# 用非递归的方式反转单链表


class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None


def linklist_init(data):
    if not isinstance(data, list) or len(data) == 0:
        raise Exception('Params Error')
    head = Node(data[0])
    tail = head
    for d in data[1:]:
        node = Node(d)
        tail.next = node
        tail = tail.next
    return head


def display(head):
    if not isinstance(head, Node):
        raise Exception('Params Error')
    while head:
        # print(head.data)
        head = head.next


def reverse(head):
    stack = list()
    while head:
        stack.append(head.data)
        head = head.next
    while len(stack) > 0:
        data = stack.pop()
        print(data)


if __name__ == '__main__':
    head = linklist_init([i * i for i in range(10)])
    display(head)
    reverse(head)