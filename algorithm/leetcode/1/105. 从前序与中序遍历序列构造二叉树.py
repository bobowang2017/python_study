# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.tag = 0

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        length = len(preorder)
        return self.build(preorder, inorder, 0, 0, length - 1)

    def build(self, preorder, inorder, tag, s, e):
        if s > e:
            return None
        root_val = preorder[self.tag]
        root = None
        i = s
        while i <= e:
            if root_val == inorder[i]:
                root = TreeNode(root_val)
                self.tag += 1
                root.left = self.build(preorder, inorder, tag, s, i - 1)
                root.right = self.build(preorder, inorder, tag, i + 1, e)
                break
            i += 1
        return root
