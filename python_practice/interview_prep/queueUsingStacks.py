class QueueUsingStack:
    def __init__(self):
        self.stack = []
        self.temp = []

    def push(self, value):
        while self.temp:
            self.stack.append(self.temp.pop())
        self.stack.append(value)

    def pop(self):
        if self.stack is None:
            return "Stack is empty"
        while self.stack:
            self.temp.append(self.stack.pop())
        return self.temp.pop()

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        if len(self.stack):
            return False
        else:
            return True



arr = [1, 2, 3, 4, 5]


def aa(arr):
    if arr:
        return arr[0]

print(aa(arr))
print(arr)