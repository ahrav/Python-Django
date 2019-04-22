class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def divide(self, head):
        if head is None:
            return None
        runner = head
        current = head
        while runner is not None:
            runner = runner.next
            if runner is None:
                break
            runner = runner.next
            current = current.next
        to_return = current.next
        current.next = None
        return to_return