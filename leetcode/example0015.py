# -*- coding: utf-8 -*-

# 给定一个二叉树，返回它的中序 遍历。


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root.left is None and root.right is None:
            return []
        result = []
        if root.left:
            result += self.inorderTraversal(root.left)
        # print(root.val)
        result.append(root.val)
        if root.right:
            result += self.inorderTraversal(root.right)
        return result


if __name__ == '__main__':
    s = Solution()
    data = s.inorderTraversal([])
    print(data)
