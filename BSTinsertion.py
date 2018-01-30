'''create a binary search and insertion function'''

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        current = self.root
        found = False
        while current.left or current.right:
            if new_val.value <= current.value:
                new_val.left = current.left
                current.left = new_val
            else:
                new_val.right = current.right
                current.right = new_val

    def search(self, find_val):
        current = self.root
        if current.value == find_val:
                return True
        while current.left or current.right:
            if current.value == find_val:
                return True
            if find_val < current.value:
                current = self.left
            else:
                current = self.right
        return False

# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)
