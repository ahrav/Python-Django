class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

def reverse(head):
    if head.next is None:
        return head
    curr = head
    prev = None
    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev