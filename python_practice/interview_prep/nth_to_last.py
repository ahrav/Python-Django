class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def nth_to_last(self, head, n):
        follower = head
        current = head
        for i in range(n-1):
            if current.next is None:
                return None
            current = current.next
        while current and current.next:
            current = current.next
            follower = follower.next
        return follower
