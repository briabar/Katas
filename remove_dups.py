class Node(object):
    def __init__(self, data, next=False):
        self.data = data
        self.next = next

def print_list(head):
    current = head
    while current.next:
        print current.data
        current = current.next
    print current.data


def remove_dups(head):
    if not head.next:
        return
    current = head
    chk = set([current.data])
    while current.next:
        if current.next.data in chk:
            current.next = current.next.next
        else:
            chk.add(current.next.data)
            current = current.next
    print_list(head)

'''Mistake: was updating pointer even in case of "if current.next.data in chk:"
this led to node hopping.'''


node_5 = Node(4)
node_4 = Node(3, node_5)
node_3 = Node(3, node_4)
node_2 = Node(2, node_3)
node_1 = Node(1, node_2)

print("#######BEFORE REMOVAL########")
print_list(node_1)
print("########AFTER REMOVAL########")

remove_dups(node_1)
