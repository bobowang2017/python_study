from binary_tree.tree import Tree


class NodeNumbers(object):

    def all(self, root):
        """
        二叉树的节点个数
        :param root:
        :return:
        """
        if not root:
            return 0
        left_nums = self.all(root.lchild)
        right_nums = self.all(root.rchild)
        return left_nums + right_nums + 1

    def all_leave(self, root):
        """
        所有叶子节点个数
        :param root:
        :return:
        """
        if not root:
            return 0
        if root.lchild is None and root.rchild is None:
            return 1
        return self.all_leave(root.lchild) + self.all_leave(root.rchild)

    def k_nums(self, root, k):
        """
        第K层节点个数
        :param root:
        :return:
        """
        if not root or k < 1:
            return 0
        if k == 1:
            return 1
        left_nums = self.k_nums(root.lchild, k - 1)
        right_nums = self.k_nums(root.rchild, k - 1)
        return left_nums + right_nums


if __name__ == '__main__':
    tree = Tree()
    for i in range(1, 11):
        tree.add(i)
    display = NodeNumbers()
    # result = display.all(tree.root)
    # result = display.all_leave(tree.root)
    result = display.k_nums(tree.root, 4)
    print(result)
