def sortedInsert(head, data):
    node = Node(data)
    if head is None:
        return node
    currentNode = head
    while currentNode.next is not None:
        if node.data >= currentNode.data and node.data <= currentNode.next.data:
            currentNode.next.prev = node
            node.next = currentNode.next
            currentNode.next = node
            return head
        currentNode = currentNode.next
    node.prev = currentNode
    currentNode.next = node
    return head

