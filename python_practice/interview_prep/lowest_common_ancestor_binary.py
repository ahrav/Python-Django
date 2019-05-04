class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def lca(tree, n1, n2):
    if n1 == n2:
        return n1
    path_to_n1 = path_to_node(tree, n1)
    path_to_n2 = path_to_node(tree, n2)
    if not path_to_n1 or not path_to_n2:
        return None
    prev = None
    while path_to_n1 and path_to_n2:
        s = path_to_n1.pop(0)
        t = path_to_n2.pop(0)
        if s == t:
            prev = s
        else:
            break
        return prev

def path_to_node(tree, n):
    if not tree:
        return None
    if tree == n:
        stack = []
        stack.append(tree)
        return stack
    left = path_to_node(tree.left, n)
    right = path_to_node(tree.right, n)

    if left:
        left.push(tree)
        return left
    if right:
        right.push(tree)
        return right
    return None
