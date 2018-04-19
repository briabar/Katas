from collections import deque
class Tree(object):
    def __init__(self, node):
        self.head = node

    def print_BST(self):
        if not self.head:
            print "no head"
        current = self.head
        q = deque()
        q.append(current)
        while q:            ##WHAT IS WRONG HERE?!
            current = q.popleft()
            if current != None:
                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)


class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def make_BST(array, start, end):
    if end < start:
        return -1
    mean = (start + end) / 2
    node = Node(array[mean])
    node.left = make_BST(array, start, mean - 1)
    node.right = make_BST(array, mean + 1, end)
    return node


array = [0,1,2,3,4,5,6,7,8,9,10]

tree = Tree(make_BST(array, 0, len(array)-1))


class LLNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):
    def __init__(self, node):
        self.head = node


class ListBucket(object):
    def __init__(self, head):
        self.head = [head]
    def add(self, head):
        self.head.append(head)


def list_of_depths(tree):
    current = tree.head
    q = deque()
    q.append(current)
    ListBucket(LinkedList(LLNode(current.data)))
    low = current.data
    high = current.data
    while q:
        current = q.popleft()
        if current.left():
            if current.left < low:
                ListBucket(LinkedList(LLNode(current.left.data)))

            q.append(current.left)
        if current.right():
            q.append(current.left)
#
#
#   5
#  |  \
#  3   7
# | \  | \
# 2  4 6  8
