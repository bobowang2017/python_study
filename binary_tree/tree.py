
class Node(object):

    def __init__(self, item):
        self.lchild = None
        self.rchild = None
        self.item = item


class Tree(object):
    def __init__(self):
        self.root = None

    def add(self, item):
        node = Node(item)
        if not self.root:
            self.root = node
        else:
            queue = [self.root]
            while True:
                pop_node = queue.pop(0)
                if not pop_node.lchild:
                    pop_node.lchild = node
                    return
                elif not pop_node.rchild:
                    pop_node.rchild = node
                    return
                else:
                    queue.append(pop_node.lchild)
                    queue.append(pop_node.rchild)



# if __name__ == '__main__':
#     tree = Tree()
#     for i in range(1,11):
#         tree.add(i)
#     print(tree)

