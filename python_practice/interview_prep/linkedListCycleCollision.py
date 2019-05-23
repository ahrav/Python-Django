class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None

def beginning(head):
    slow = head
    fast = head
    while fast.next is not None and fast is not None:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            break
    if fast is None and fast.next is None:
        return None
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return fast
    