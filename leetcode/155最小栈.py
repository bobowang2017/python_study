# 设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。
#
# push(x) -- 将元素 x 推入栈中。
# pop() -- 删除栈顶的元素。
# top() -- 获取栈顶元素。
# getMin() -- 检索栈中的最小元素。


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = None

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.min or x < self.min:
            self.min = x
        self.stack.append((x, self.min))

    def pop(self):
        """
        :rtype: void
        """
        return self.stack.pop()[0]

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1][1]


obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
param_4 = obj.getMin()
obj.pop()
param_3 = obj.top()
param_5 = obj.getMin()
print(param_3)
print(param_4)
print(param_5)
