# 给定一个二叉树，它的每个结点都存放一个 0-9 的数字，每条从根到叶子节点的路径都代表一个数字。
# 例如，从根到叶子节点路径 1->2->3 代表数字 123。
# 计算从根到叶子节点生成的所有数字之和。
# 说明: 叶子节点是指没有子节点的节点。
# 示例 1:
# 输入: [1,2,3]
#     1
#    / \
#   2   3
# 输出: 25
# 解释:
# 从根到叶子节点路径 1->2 代表数字 12.
# 从根到叶子节点路径 1->3 代表数字 13.
# 因此，数字总和 = 12 + 13 = 25.


class Solution(object):
    def display(self, root, sum, result):
        if not root:
            return
        if not root.left and not root.right:
            result.append(sum * 10 + root.val)
            return
        if root.left:
            self.display(root.left, sum * 10 + root.val, result)
        if root.right:
            self.display(root.right, sum * 10 + root.val, result)
        return

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = []
        self.display(root, 0, result)
        return sum(result)
