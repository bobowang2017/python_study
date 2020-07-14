# -*- coding: utf-8 -*-
from collections import deque


class MaxQueue(object):

    def __init__(self):
        self.data = []
        self.Q = deque()

    def max_value(self):
        """
        :rtype: int
        """
        return self.Q[0] if len(self.Q) else -1

    def push_back(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.data.append(value)
        while len(self.Q) > 0 and value > self.Q[-1]:
            self.Q.pop()
        self.Q.append(value)
        print(self.Q)

    def pop_front(self):
        """
        :rtype: int
        """
        if not len(self.Q):
            return -1
        data = self.data.pop(0)
        if data == self.Q[0]:
            self.Q.popleft()
        return data


s = MaxQueue()
print(s.max_value())
s.push_back(1)
s.push_back(2)
print(s.max_value())
print(s.pop_front())
print(s.max_value())

# s.push_back(3)
# s.push_back(4)
# s.push_back(8)
# s.push_back(7)
# s.push_back(12)
# s.push_back(11)
