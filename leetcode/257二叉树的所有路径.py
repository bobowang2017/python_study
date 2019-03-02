# -*- coding: utf-8 -*-
# 给定一个二叉树，返回所有从根节点到叶子节点的路径。
# 说明: 叶子节点是指没有子节点的节点。
# 示例:
# 输入:
#    1
#  /   \
# 2     3
#  \
#   5
# 输出: ["1->2->5", "1->3"]
# 解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3


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
    def __init__(self):
        self.result = []

    def display(self, root, path):
        if not root.left and not root.right:
            self.result.append((path + '->' + str(root.val))[2:])
        if root.left:
            self.display(root.left, path+'->' +str(root.val))
        if root.right:
            self.display(root.right, path+'->' +str(root.val))

    def binaryTreePaths(self, root):
        if not root:
            return []
        self.display(root, "")
        return self.result


if __name__ == '__main__':
    tree = Tree()
    for i in range(1,10):
        tree.add(i)
    s = Solution()
    s.binaryTreePaths(tree.root)
    print(s.result)
