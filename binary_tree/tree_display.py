from binary_tree.tree import Tree


class Display(object):

    def traverse(self, tree):
        """
        层序遍历
        :param tree:
        :return: None
        """
        if not tree.root:
            return
        queue = [tree.root]
        result = [tree.root.item]
        while len(queue) > 0:
            print(result)
            # result = []
            parent = queue.pop(0)
            if parent.lchild:
                queue.append(parent.lchild)
                result.append(parent.lchild.item)
            if parent.rchild:
                queue.append(parent.rchild)
                result.append(parent.rchild.item)
        return

    def preorder(self, root, result):
        """
        先序遍历
        :param tree:
        :return:
        """
        if not root:
            return
        result.append(root.item)
        self.preorder(root.lchild, result)
        self.preorder(root.rchild, result)
        return result

    def inorder(self, root, result):
        """
        中序遍历
        :param tree:
        :return:
        """
        if not root:
            return
        self.inorder(root.lchild, result)
        result.append(root.item)
        self.inorder(root.rchild, result)
        return result

    def lastorder(self, root, result):
        """
        后序遍历
        :param tree:
        :return:
        """
        if not root:
            return
        self.lastorder(root.lchild, result)
        self.lastorder(root.rchild, result)
        result.append(root.item)
        return result


if __name__ == '__main__':
    tree = Tree()
    for i in range(1, 11):
        tree.add(i)
    display = Display()
    # display.traverse(tree)
    # result = display.preorder(tree.root, [])
    # result = display.inorder(tree.root, [])
    result = display.lastorder(tree.root, [])
    print(result)
