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
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)


tree = Tree()
for data in [4, 2, 7, 1, 3, 6, 9]:
    tree.add(data)

solution = Solution()
solution.invertTree(tree.root)
print('')