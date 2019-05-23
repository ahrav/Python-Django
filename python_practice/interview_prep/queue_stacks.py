class StacksToQueue:
    def __init__(self):
        self.instack = []
        self.outstack = []

    def enqueue(self, value):
        self.instack.append(value)

    def dequeue(self):
        if self.instack is None:
            return ("Stack is empty, please enqueue before dequeueing")
        while self.instack:
            self.outstack.append(self.instack.pop())
        return self.outstack.pop()