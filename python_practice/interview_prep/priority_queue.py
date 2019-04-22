class PriorityQueue(object):
    def __init__(self):
        self.queue = []
        self.size = 0

    def is_empty(self):
        return len(self.queue) == []
    
    def insert(self, data):
        if self.size == len(self.queue):
            return "broken"
        pos = self.size
        self.queue[pos] = data

        while pos > 0:
            parent = (pos + 1) // 2 - 1
            if self.queue[parent] >= self.queue[pos]:
                break
            self.swap_indices(parent, pos)
            pos = parent
        self.size += 1

    def pop(self):
        if self.size == 0:
            return "No values in heap"
        to_return = self.queue[0]
        self.queue[0] = self.queue[self.size -1]
        self.size -= 1
        
        pos = 0
        while pos < self.size // 2:
            left_child = pos * 2 + 1
            right_child = left_child + 1
            if right_child < self.size and self.queue[left_child] < self.queue[right_child]:
                if self.queue[pos] >= self.queue[right_child]:
                    break
                self.swap_indices(pos, right_child)
                pos = right_child
            else:
                if self.queue[pos] <= self.queue[left_child]:
                    break
                self.swap_indices(pos, left_child)
                pos = left_child
        return to_return

    def swap_indices(self, i, j):
        temp = self.queue[i]
        self.queue[i] = self.queue[j]
        self.queue[j] = temp

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    def delete(self):
        try:
            max = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[max]:
                    max = i
            item = self.queue[max]
            del self.queue[max]
            return item
        except IndexError:
            print()
            exit()

g = PriorityQueue()
g.insert(5)
g.insert(2)
g.insert(10)
print (g)