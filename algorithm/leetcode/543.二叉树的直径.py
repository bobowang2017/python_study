# 给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。
#
# 示例 :
# 给定二叉树
#
#           1
#          / \
#         2   3
#        / \
#       4   5
# 返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。
#
# 注意：两结点之间的路径长度是以它们之间边的数目表示。


# 解题思路：树中节点路径长度可以理解成任何一个节点左子树高度+右子树高度，然后遍历的时候记录最大值即可。

class Solution(object):
    def __init__(self):
        self.result = 0

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.display(root)
        return self.result

    def display(self, root):
        left = self.display(root.left) if root.left else 0
        right = self.display(root.right) if root.right else 0
        self.result = max(self.result, left+right)
        return max(left, right) + 1