class ListNode(object):

    def __init__(self, data):
        self.data = data
        self.next = None

    def deleteDuplicates(linkedList):

        previousNode = linkedList.head
        currentNode = previousNode.next
        duplicates = set()

        if previousNode is None:
            return None

        while currentNode:
            if currentNode.data not in duplicates:
                duplicates.add(currentNode.data)
                previousNode = currentNode
                currentNode = currentNode.next
            else:
                previousNode.next = currentNode.next
                currentNode = currentNode.next

