# 给定一个二叉树，检查它是否是镜像对称的。
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
#     1
#    / \
#   2   2
#    \   \
#    3    3


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def is_mirror(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        return self.is_mirror(left.left, right.right) and self.is_mirror(left.right, right.left)

    def isSymmetric(self, root):
        if not root:
            return True
        if (not root.left and root.right) or (root.left and not root.right):
            return False
        return self.is_mirror(root.left, root.right)
