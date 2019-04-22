class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def cycle_check(self, head):
        visited_nodes = set()

        temp = head
        while temp:
            if self.value in visited_nodes:
                return True
            else:
                visited_nodes.add(self.value)
                temp = temp.next
        return False

    def cycle_check_floyd(self, head):
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False