class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

def is_balanced(node):
    if balanced_height(node) > -1:
        return True
    return False

def balanced_height(node):
    if node is None:
        return 0
    h1 = balanced_height(node.left)
    h2 = balanced_height(node.right)
    if h1 == -1 or h2 == -1:
        return -1
    if abs(h1-h2) > 1:
        return -1
    if h1 > h2:
        return h1 + 1
    else:
        return h2 + 1