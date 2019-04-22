class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    class LinkedList:
        
        def __init__(self):
            self.head = None

        def push(self, new_data):
            new_node = Node(new_data)
            new_node.next = self.head
            self.head = new_node

        def printMiddle(self):
            slow_ptr = self.head
            fast_ptr = self.head

            if self.head is not None:
                while (fast_ptr is not None and fast_ptr.next is not None):
                    fast_ptr = fast_ptr.next.next
                    slow_ptr = slow_ptr.next
                return slow_ptr.data