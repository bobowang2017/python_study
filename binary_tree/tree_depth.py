from binary_tree.tree import Tree


class Depth(object):

    def max_depth(self, root):
        if not root:
            return 0
        left_depth = self.max_depth(root.lchild)
        right_depth = self.max_depth(root.rchild)
        return max(left_depth, right_depth) + 1

    def min_depth(self, root):
        if not root:
            return 0
        left_depth = self.max_depth(root.lchild)
        right_depth = self.max_depth(root.rchild)
        return 1 + min(left_depth, right_depth) if left_depth and right_depth else 1 + left_depth + right_depth


if __name__ == '__main__':
    tree = Tree()
    for i in range(1, 11):
        tree.add(i)
    display = Depth()
    result = display.min_depth(tree.root)
    print(result)
