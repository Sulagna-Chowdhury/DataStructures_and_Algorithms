def check_is_symmetric_tree(tree)->bool:

    def is_symmetric(left_tree:BinaryTreeNode, right_tree:BinaryTreeNode) -> bool:
        if not left_tree and not right_tree:
            return True
        elif left_tree and right_tree:
            return (left_tree.data == right_tree.data and
                    is_symmetric(left_tree.left, right_tree.right) and
                    is_symmetric(left_tree.right, right_tree.left))
        else:
            return False

    return is_symmetric(tree.left, tree.right)


class BinaryTreeNode:
    def __init__(self, left=None, right=None, data=None, parent=None):
        self.left = left
        self.right = right
        self.data = data
        self.parent = parent

def tree_example1():
    e = BinaryTreeNode(data='e')
    f = BinaryTreeNode(data='f')
    d = BinaryTreeNode(data='d', left=e, right=f)
    e.parent = d
    f.parent = d

    g = BinaryTreeNode(data='g')
    c = BinaryTreeNode(data='c', left=d, right=g)
    d.parent = c
    g.parent = c

    i = BinaryTreeNode(data='i')
    j = BinaryTreeNode(data='j')
    h = BinaryTreeNode(data='d', left=i, right=j)
    i.parent = h
    j.parent = h

    b = BinaryTreeNode(data='b', left=c, right=h)
    c.parent = b
    h.parent = b

    m = BinaryTreeNode(data='m')
    n = BinaryTreeNode(data='n')
    l = BinaryTreeNode(data='l', left=m, right=n)
    m.parent = l
    n.parent = l

    o = BinaryTreeNode(data='o')
    k = BinaryTreeNode(data='k', left=l, right=o)
    l.parent = k
    o.parent = k

    a = BinaryTreeNode(data='a', left=b, right=k)
    b.parent = a
    k.parent = a
    return a

def tree_example3():
    f = BinaryTreeNode(data='5')
    g = BinaryTreeNode(data='6')
    e = BinaryTreeNode(data='4', left=f, right=g)
    f.parent = e
    g.parent = e

    d = BinaryTreeNode(data='3')
    b = BinaryTreeNode(data='2', left=d, right = e)
    d.parent = b
    e.parent = b

    j = BinaryTreeNode(data='6')
    k = BinaryTreeNode(data='5')
    i = BinaryTreeNode(data='4', left=j, right=k)
    j.parent = i
    k.parent = i

    l = BinaryTreeNode(data='3')
    c = BinaryTreeNode(data='2', left=i, right=l)
    i.parent = c
    l.parent = c

    a = BinaryTreeNode(data='1', left=b, right=c)
    b.parent = a
    c.parent = a

    return a

if __name__ == '__main__':
    tree1 = tree_example1()

    tree3 = tree_example3()

    tree1_symmetric = check_is_symmetric_tree(tree1)
    tree3_symmetric = check_is_symmetric_tree(tree3)

    print('Tree 1 symmetric :', tree1_symmetric)
    print('Tree 3 symmetric :', tree3_symmetric)