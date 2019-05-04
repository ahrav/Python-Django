class Node:
    def __init__(self):
        self.next = None
        self.random = None

def clone(n):
    if n is None:
        return n
    n_curr = n
    while n_curr is not None:
        temp = Node()
        temp.next = n_curr.next
        n_curr.next = temp
        n_curr.next = n_curr.next.next

    n_curr = n
    while n_curr is not None:
        n_curr.next.random = n_curr.random.next
        n_curr = n_curr.next.next

    temp = n.next
    n_curr = n
    while n_curr.next is not None:
        n_curr.next = n_curr.next.next
    return temp