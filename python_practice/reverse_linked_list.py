class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    class LinkedList:
        

        def __init__(self, data):
            self.data = data
            self.head = None

        def reverse(self, head):
            current = head
            previous = None
            next_node = None

            while current:
                next_node = current.next
                current.next = previous
                previous = current
                current = next_node

            return previous
