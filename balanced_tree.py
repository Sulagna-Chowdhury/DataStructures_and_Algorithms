import collections

def is_balanced_binary_tree(tree):
    """
    Balanced Tree : Difference between height for each node between the left and right sub-tree is at max 1.
    """
    Balanced_Height = collections.namedtuple('Balanced_Height',('balanced', 'height'))

    def check_balanced(tree):

        if not tree: # Base Case - left or right child of left node.
            return Balanced_Height(True, -1)

        left_check = check_balanced(tree.left)
        if not left_check.balanced: # If the left sub-tree is not balanced
            return Balanced_Height(False, 0)

        right_check = check_balanced(tree.right)
        if not right_check.balanced:  # If the right sub-tree is not balanced
            return Balanced_Height(False, 0)

        is_balanced = abs(left_check.height - right_check.height) <= 1
        heigth = max(left_check.height,right_check.height)+1 if is_balanced else 0

        return Balanced_Height(is_balanced, heigth)

    return check_balanced(tree).balanced

class BinaryTreeNode:
    def __init__(self,left = None, right = None, data = None, parent = None):
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

def tree_example2():
    d = BinaryTreeNode(data='d')
    e = BinaryTreeNode(data='e')
    c = BinaryTreeNode(data='c', left=d, right=e)
    d.parent = c
    e.parent = c

    h = BinaryTreeNode(data='h')
    g = BinaryTreeNode(data='g',left = h)
    h.parent = g

    f = BinaryTreeNode(data='f',right = g)
    g.parent = f

    b = BinaryTreeNode(data='b', left=c, right=f)
    c.parent = b
    f.parent = b

    m = BinaryTreeNode(data='m')
    l = BinaryTreeNode(data='l', right = m)
    m.parent = l

    n = BinaryTreeNode(data='n')
    k = BinaryTreeNode(data='k', left = l, right = n)
    l.parent = k
    n.parent = n

    j = BinaryTreeNode(data='j', right = k)
    k.parent = j

    p = BinaryTreeNode(data='p')
    o = BinaryTreeNode(data='o',right = p)

    i = BinaryTreeNode(data='i',left = j,right = o)
    j.parent = i
    o.parent = i

    a = BinaryTreeNode(data='a',left = b,right = i)
    b.parent = a
    i.parent = a

    return a

if __name__ == '__main__':
    tree1 = tree_example1()

    tree2 = tree_example2()

    tree1_balanced = is_balanced_binary_tree(tree1)
    tree2_balanced = is_balanced_binary_tree(tree2)

    print('Tree 1 balanced :',tree1_balanced)
    print('Tree 2 balanced :',tree2_balanced)