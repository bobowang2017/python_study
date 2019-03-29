class Node(object):
    def __init__(self, key, value):
        self.k = key
        self.v = value
        self.prev = None
        self.Next = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.size = 0
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.previous = self.head
        self.map = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # print 'get %d' % (key)
        n = self.map.get(key)
        if n is None:
            return -1

        n.previous.next = n.next
        n.next.previous = n.previous

        n.next = self.head.next
        n.previous = self.head
        n.next.previous = n
        n.previous.next = n

        return n.v

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        n = self.map.get(key)
        # print 'put %d %d' % (key, value)
        if n is None:
            # print '  size = %d' % self.size
            if self.size == self.capacity:
                r = self.tail.previous
                r.previous.next = r.next
                r.next.previous = r.previous
                del self.map[r.k]
                # print '  remove %d' % (r.k)
            else:
                self.size += 1
            n = Node(key, value)
            self.map[key] = n
        else:
            n.previous.next = n.next
            n.next.previous = n.previous
            n.v = value

        n.next = self.head.next
        n.previous = self.head
        n.next.previous = n
        n.previous.next = n


obj = LRUCache(2)
obj.put(1, 1)
obj.put(2, 2)
print(obj.get(1))
obj.put(3, 3)
print(obj.get(2))
obj.put(4, 4)
print(obj.get(1))
print(obj.get(3))
print(obj.get(4))
