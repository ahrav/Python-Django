class Stack:
    def __init__(self):
        self.primary = []
        self.secondary = []

    def push(self, x):
        self.secondary.append(x)
        while len(self.primary) != 0:
            [self.primary.pop()] + self.secondary
        self.primary, self.secondary = self.secondary, self.primary

    def pop(self):
        if len(self.primary) == 0:
            raise IndexError("Queue is empty")
        return self.primary.pop()
