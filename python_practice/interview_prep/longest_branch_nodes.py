class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def consecutive(n, prev=None, length=None):
    if n is None:
        return length
    if n.value == prev+1:
        left_length = consecutive(n.left, n.value, length+1)
        right_length = consecutive(n.right, n.value, length+1)
        return max(left_length, right_length)
    else:
        left_length = consecutive(n.left, n.value, 1)
        right_length = consecutive(n.right, n.value, 1)
        return max(left_length, right_length, length)
    return max(consecutive(n.left, n.value, 1), consecutive(n.right, n.value, 1))


