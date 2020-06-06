# -*- coding: utf-8 -*-
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):

    def is_same_tree(self, s, t):
        if not s and not t:
            return True
        if not t or not s:
            return False
        if s.val != t.val:
            return False
        return self.is_same_tree(s.left, t.left) and self.is_same_tree(s.right, t.right)

    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s:
            return False
        return self.is_same_tree(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)