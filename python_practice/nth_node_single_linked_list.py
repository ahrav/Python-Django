class Node:

    def __init__(self, data):
        self.data = data
        self.next_node = None

    class LinkedList:

        def __init__(self):
            self.head = None

        def nth_to_last(linkedList, n):
            left_pointer = linkedList.head
            right_pointer = linkedList.head

            for i in range(n-1):
                if not right_pointer.nextNode:
                    raise LookupError('Error: n i larger than the linked list')
                right_pointer = right_pointer.next_node

            while right_pointer.next_node:
                right_pointer = right_pointer.next_node
                left_pointer = left_pointer.next_node
            return left_pointer