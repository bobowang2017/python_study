class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.tag = 0

    def buildTree(self, inorder, postorder):
        """
        :type preorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        length = len(inorder)
        self.tag = length - 1
        return self.build(inorder, postorder, 0, length - 1)

    def build(self, inorder, postorder, s, e):
        if s > e:
            return None
        root_val = postorder[self.tag]
        root = None
        i = s
        while i <= e:
            if root_val == inorder[i]:
                root = TreeNode(root_val)
                self.tag -= 1
                root.right = self.build(inorder, postorder, i + 1, e)
                root.left = self.build(inorder, postorder, s, i - 1)
                break
            i += 1
        return root


s = Solution().buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3])
print(s)
