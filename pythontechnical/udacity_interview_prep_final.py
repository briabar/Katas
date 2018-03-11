import Queue as Q

def question1(s,t):
    '''Given two strings s and t, determine whether some anagram of t is a substring
    of s. For example: if s = "udacity" and t = "ad", then the function returns
    True. Your function definition should look like: question1(s, t) and return a
    boolean True or False.'''
    if len(t) > len(s):
        return False
    front = 0
    back = len(t)
    while back <= len(s):
        if set(s[front:back]) == set(t):
            return True
        else:
            front += 1
            back += 1
    return False

print(question1("udacity", ""))  #True
print(question1("chicken is the  best meat money can buy", "uy"))  #True
print(question1("a", "chicken is the  best meat money can buy"))  #False
print(question1("", "asd"))  #False


# Question 2
def question2(a):
    """Given a string a, find the longest palindromic substring contained in a.
    Your function definition should look like question2(a), and return a
    string."""
    a = a.replace(" ", "")
    list_of_pal = []
    if a == a[::-1]:
        return a
    if len(a) <= 1:
        return a
    ix = 0
    #check2
    while ix < len(a) - 1:
        if a[ix] == a[ix+1]:
            list_of_pal.append([ix,ix + 1])
        if ix + 2 <= len(a)-1:
            if a[ix:ix+2] == a[ix+2:ix:-1]:
                list_of_pal.append([ix, ix + 1, ix + 2])
        ix += 1
    ix = 0
    result = []
    for starts in list_of_pal:
        is_pal = True
        front = starts[0]
        end = starts[-1]
        while is_pal:
            result.append([len(starts), sorted(starts)])
            if front - 1 >= 0 and end + 1 <= len(a) - 1:
                if a[front - 1] == a[end + 1]:
                    starts.extend([front - 1, end + 1])
                    front -= 1
                    end += 1
                else: is_pal = False
            else: is_pal = False
    if result ==[]:
        return -1
    result = sorted(result)
    return a[result[-1][1][0]:result[-1][1][-1]+1]


print(question2("cattaccattacblskddidmmooommm")) #cattaccattac
print(question2("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")) # all of this
print(question2("123456789")) #-1


def question3(G):
    '''Given an undirected graph G, find the minimum spanning tree within G.
    A minimum spanning tree connects all vertices in a graph with the smallest
    possible total weight of edges. Your function should take in and return an
    adjacency list structured like this:
    {'A': [('B', 2)],
     'B': [('A', 2), ('C', 5)],
     'C': [('B', 5)]}'''
    q = Q.PriorityQueue()
    result = {}
    for node in G:
        for edge in G[node]:
            q.put((edge[1], node, edge[0]))
    while not q.empty():
        lightest_edge = q.get()
        if lightest_edge[1] not in result:
            result[lightest_edge[1]] = (lightest_edge[2], lightest_edge[0])
    print result

question3({'A': [('B', 2), ('C', 2), ('E', 7)],
      'B': [('A', 2), ('D', 5)],
      'C': [('A', 2), ('E', 2)],
      'D': [('B', 5), ('F', 10)],
      'E': [('A', 7), ('C', 2)],
      'F': [('D', 10)]})  #{'A': ('B', 2), 'C': ('A', 2), 'B': ('A', 2), 'E': ('C', 2), 'D': ('B', 5), 'F': ('D', 10)}

question3({'A': [('B', 1), ('C', 1), ('D', 1)],
      'B': [('A', 1)],
      'C': [('A', 1)],
      'D': [('A', 1)],})  #{'A': ('B', 1), 'C': ('A', 1), 'B': ('A', 1), 'D': ('A', 1)}

question3({})  #{}

def question4(T, r, n1, n2):
    '''Find the least common ancestor between two nodes on a binary search tree.
    The least common ancestor is the farthest node from the root that is an
    ancestor of both nodes. For example, the root is a common ancestor of all
    nodes on the tree, but if both nodes are descendents of the root's left
    child, then that left child might be the lowest common ancestor. You can
    assume that both nodes are in the tree, and the tree itself adheres to all
    BST properties. The function definition should look like
    question4(T, r, n1, n2), where T is the tree represented as a matrix,
    where the index of the list is equal to the integer stored in that
    node and a 1 represents a child node, r is a non-negative integer
    representing the root, and n1 and n2 are non-negative integers representing
    the two nodes in no particular order. For example, one test case might be

    question4([[0, 1, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [1, 0, 0, 0, 1],
              [0, 0, 0, 0, 0]],
             3,
             1,
             4)'''
    parent_nodes = []
    while n1 != r:
        n1 = get_parent(T, n1)
        if n1 == "error":
            return n1
        parent_nodes.append(n1)
    if len(parent_nodes) == 0:
        return "error"
    while n2 != r:
        n2 = get_parent(T, n2)
        if n2 == "error":
            return n2
        if n2 in parent_nodes:
            return n2
    return "error"


def get_parent(T, n):
    for i in range(0, len(T)):
        if T[i][n] == 1:
            return i
    return "error"


print question4([[0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]],
          3,
          1,
          4)  #3

print question4([[0, 0, 0, 0, 0],
           [0, 0, 0, 1, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 0],
           [0, 1, 1, 0, 0]],
          4,
          1,
          3)  #4

print question4([[0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0]],
          3,
          1,
          4)  #error
# Question 5
#
# Find the element in a singly linked list that's m elements from the end.
# For example, if a linked list has 5 elements, the 3rd element from the end is
# the 3rd element. The function definition should look like question5(ll, m),
# where ll is the first node of a linked list and m is the "mth number from the
# end". You should copy/paste the Node class below to use as a representation of
# a node in the linked list. Return the value of the node at that position.
class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def question5(self, m):
        '''I chose to make this a class method instead of a seperate function
        I figure it makes the code a lot more clean. This works in O(n) time.'''
        if not self.head:
            print "linked list contains no nodes"
            return -1
        current = self.head
        array = [current.data]
        while current.next:
            current = current.next
            array.append(current.data)
        if len(array) < m:
            print "no item at position %s" % m
            return -1
        print array[-m]

nodes = [Node(1),
         Node("two"),
         Node(3),
         Node("pizza"),
         Node(5),
         Node(6)]

nodes2 = [Node(1)]

nodes3 = []

ll = LinkedList()
ll2 = LinkedList()
ll3 = LinkedList()


for node in nodes:
    ll.append(node)
for node in nodes2:
    ll2.append(node)
for node in nodes3:
    ll3.append(node)

ll.question5(3)  #pizza
ll2.question5(3)  #pizza
ll3.question5(3)  #pizza
