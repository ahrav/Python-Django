class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

        class LinkedList:
            
            def __init__(self, data)
            self.head = None

            def cycle_check(node):

                marker1 = node
                marker2 = node

                while marker2 != None and marker2.next != None:

                    marker1 = marker1.next
                    marker2 = marker2.next.next

                    if marker2 == marker1:
                        return True
                
                return False

            def cycle_check_two (self):
                s = set()
                temp = self.head

                while (temp):
                    if (temp in s):
                        return True
                    s.add(current)
                    temp = temp.next
                return False

