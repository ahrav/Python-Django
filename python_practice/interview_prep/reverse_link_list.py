class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def print_reversed_list(node):
    if node == None:
        return
    print_reversed_list(node.next)
    print (node.value)


a = Node(1)
b = Node(2)
c = Node(3)
a.next = b
b.next = c

print_reversed_list(a)