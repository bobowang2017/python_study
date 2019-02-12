from binary_tree.tree import Tree


class TreeJudge(object):

    def is_balance_tree(self, root):
        """
        是否是平衡二叉树
        :param root:
        :return:
        """
        if not root:
            return 0
        left = self.is_balance_tree(root.lchild)
        right = self.is_balance_tree(root.rchild)
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return max(left, right) + 1

    def is_complete_tree(self, root):
        """
        判断二叉树是否是完全二叉树
        1、树为空，直接报错
        2、层序遍历二叉树（2.1、如果一个结点左右孩子都不为空，则pop该节点，将其左右孩子入队列；
                          2.2、如果遇到一个结点，左孩子为空，右孩子不为空，则该树一定不是完全二叉树；
                          2.3>如果遇到一个结点，左孩子不为空，右孩子为空；或者左右孩子都为空；
                          则该节点之后的队列中的结点都为叶子节点；该树才是完全二叉树，否则就不是完全二叉树；

        :param root:
        :return:
        """
        pass

    def is_same_tree(self, t1, t2):
        """
        判断两个二叉树是否完全相同
        :param t1:
        :param t2:
        :return:
        """
        if t1 is None and t2 is None:
            return True
        elif t1 is None or t2 is None:
            return False
        if t1.item != t2.item:
            return False
        left = self.is_same_tree(t1.lchild, t2.lchild)
        right = self.is_same_tree(t1.rchild, t2.rchild)
        return left & right


if __name__ == '__main__':
    tree = Tree()
    for i in range(1, 11):
        tree.add(i)
    judge = TreeJudge()
    result = judge.is_balance_tree(tree.root) != -1
    print(result)
