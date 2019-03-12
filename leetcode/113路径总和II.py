# 给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。
# 说明: 叶子节点是指没有子节点的节点。
# 示例: 给定如下二叉树，以及目标和 sum = 22，
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \      \
#         7    2      1
# 返回:
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def display(self, root, sum, path, result):
        if not root:
            return
        path = path+','+str(root.val)
        if root.val == sum and not root.left and not root.right:
            result.append([int(p) for p in path.split(',')[1:]])
        if root.left:
            self.display(root.left, sum - root.val, path, result)
        if root.right:
            self.display(root.right, sum - root.val, path, result)

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return []
        result = []
        self.display(root, sum, "", result)
        return result
