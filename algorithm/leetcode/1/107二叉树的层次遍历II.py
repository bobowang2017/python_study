class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Tree(object):
    def __init__(self):
        self.root = None

    def add(self, item):
        node = TreeNode(item)
        if not self.root:
            self.root = node
        else:
            queue = [self.root]
            while True:
                pop_node = queue.pop(0)
                if not pop_node.left:
                    pop_node.left = node
                    return
                elif not pop_node.right:
                    pop_node.right = node
                    return
                else:
                    queue.append(pop_node.left)
                    queue.append(pop_node.right)


class Solution(object):

    def levelOrderBottom(self, root):
        if not root:
            return []
        result = [[root.val]]
        stack = [root]
        while len(stack) != 0:
            temp_stack = []
            for data in stack:
                if not data.left and not data.right:
                    continue
                if data.left:
                    temp_stack.append(data.left)
                if data.right:
                    temp_stack.append(data.right)
            stack = temp_stack
            if len(stack)!=0:
                result.insert(0, [s.val for s in stack])
        return result


if __name__ == '__main__':
    tree = Tree()
    for i in range(1, 11):
        tree.add(i)
    solution = Solution()
    result = solution.levelOrderBottom(tree.root)
    print(result)
