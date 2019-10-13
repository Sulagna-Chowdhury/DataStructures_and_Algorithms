
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

def tree_traversal(root : BinaryTreeNode) -> None:
    if root:
        print('root :',root, type(root))
        print('Preorder :', root.data,' ')
        tree_traversal(root.left)
        print('Inorder :', root.data,' ')
        tree_traversal(root.right)
        print('Postorder :',root.data,' ')

def inorder_tree_traversal(root : BinaryTreeNode) -> None:
    if root :
        inorder_tree_traversal(root.left)
        print(root.data, end= ' ,')
        inorder_tree_traversal(root.right)

def preorder_tree_traversal(root : BinaryTreeNode) -> None:
    if root :
        print(root.data,end = ' ,')
        preorder_tree_traversal(root.left)
        preorder_tree_traversal(root.right)

def post_tree_traversal(root : BinaryTreeNode) -> None:
    if root :
        post_tree_traversal(root.left)
        post_tree_traversal(root.right)
        print(root.data, end = ' ,')



if __name__ == '__main__':
    # print(a.left.data)
    # tree_traversal(a)
    a = tree_example2()
    print(' Inorder traversal :',end = '')
    inorder_tree_traversal(a)
    print(' ')
    print(' Preorder traversal :', end = '')
    preorder_tree_traversal(a)
    print(' ')
    print(' Postorder  traversal :', end = '')
    post_tree_traversal(a)