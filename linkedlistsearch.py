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
        current = self.head
        array = [current.data]
        while current.next:
            current = current.next
            array.append(current.data)
        print array[-m]

nodes = [Node(1),
         Node("two"),
         Node(3),
         Node("pizza"),
         Node(5),
         Node(6)]

ll = LinkedList()

for node in nodes:
    ll.append(node)

ll.question5(3)
