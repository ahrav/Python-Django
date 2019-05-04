class QueueNode:
    def __init__(self, array, index, value):
        self.array = array
        self.index = index
        self.value = value

    def compare_to(self, n):
        if n.value > self.value:
            return 1
        if n.value < self.value:
            return -1
        else:
            return 0

def merge(arrays):
    pq = []
    size = 0
    for i in range(len(arrays)):
        size += len(arrays[i])
        if len(arrays[i]) > 0:
            pq.append(QueueNode(i, 0, arrays[i][0]))

    results = [] * size
    for i in range(size):
        n = pq.pop(0)
        results[i] = n.value
        newIndex = n.index + 1
        if newIndex < len(arrays[n.array]):
            pq.append(QueueNode(n.array, newIndex, arrays[n.array][newIndex]))
    return results