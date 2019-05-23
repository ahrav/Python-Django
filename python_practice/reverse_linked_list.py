class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    

    def __init__(self, data):
        self.data = Node(data)
        self.length = 1

    def reverse(self, head):
        current = head
        previous = None

        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        return previous
