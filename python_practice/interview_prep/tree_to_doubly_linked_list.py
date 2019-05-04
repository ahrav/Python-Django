class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def concatenate(a, b):
    if a is None:
        return b
    if b is None:
        return a
    a_end = a.right
    b_end = b.right

    a.left = b_end
    b_end.right = a
    a_end.right = b
    b.left = a_end
    return a

def tree_to_list(n):
    if n is None:
        return n
    left_list = tree_to_list(n.left)
    right_list = tree_to_list(n.right)
    n.left = n
    n.right = n

    n = concatenate(left_list, n)
    n = concatenate(n, right_list)
    return n