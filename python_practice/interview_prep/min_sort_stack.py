class Stack:
    def __init__(self):
        self.ordered_stack = []
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def min_sort(self):
        temp = 0
        self.ordered_stack.append(self.stack.pop(0))
        while self.stack:
            temp = self.stack.pop(0)
            while self.ordered_stack and temp < self.ordered_stack[0]:
                self.stack.insert(0, self.ordered_stack.pop(0))
            self.ordered_stack.insert(0, temp)
        return self.ordered_stack

stack = Stack()
stack.push(5)
stack.push(8)
stack.push(1)
stack.push(3)

print(stack.min_sort())