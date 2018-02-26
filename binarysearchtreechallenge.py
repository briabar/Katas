

class Tree:
    def __init__(self, root):
        self.root = root
        self.left = None
        self.right = None
    def Traversal(self, root=None):
        if not root:
            root = self.root
        left = root.left
        right = root.right
        if self.left:
            self.Traversal(self.left)
        print self.root
        if self.right:
            self.Traversal(self.right)


def makeBST(a):
  if not a:
    return None
  med = len(a)//2
  root = Tree(a[med])
  root.left = makeBST(a[:med])
  root.right = makeBST(a[med+1:])
  return root




array = [1,2,3,4,5,6,7,8,11,22,33,44,55,66,77,88,99,111,222,333,444,555,666,777,888,999]

print(makeBST(array).Traversal())
