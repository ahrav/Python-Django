class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    class LinkedList:

        def __init__(self):
            self.head = None

        def length(linkeList):

            current = self.head
            count = 0

            while current:
                current = current.next
                count += 1
            return count

