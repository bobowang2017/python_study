# -*- coding: utf-8 -*-
class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.write_stack = []
        self.read_stack = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.write_stack.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if self.empty():
            return
        if self.read_stack:
            return self.read_stack.pop(-1)
        while self.write_stack:
            data = self.write_stack.pop(-1)
            self.read_stack.append(data)
        return self.read_stack.pop(-1)

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.empty():
            return
        if self.read_stack:
            return self.read_stack[-1]
        while self.write_stack:
            data = self.write_stack.pop(-1)
            self.read_stack.append(data)
        return self.read_stack[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.write_stack) + len(self.read_stack) == 0


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
param_2 = obj.peek()
print(param_2)
print(obj.pop())
param_4 = obj.empty()
print(param_4)
print(obj.pop())
print(obj.pop())
print(obj.pop())
