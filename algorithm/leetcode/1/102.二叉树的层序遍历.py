# -*- coding: utf-8 -*-
# 给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
# 示例：
# 二叉树：[3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回其层次遍历结果：
# [
#   [3],
#   [9,20],
#   [15,7]
# ]
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.queue = []
        self.result = []

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        self.queue.append(root)
        self.display()
        return self.result

    def display(self):
        while self.queue:
            count = len(self.queue)
            res_list = []
            while count > 0:
                node = self.queue.pop(0)
                print(node.val)
                res_list.append(node.val)
                if node.left:
                    self.queue.append(node.left)
                if node.right:
                    self.queue.append(node.right)
                count -= 1
            self.result.append(res_list)
